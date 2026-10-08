"""Testy generatora bibliografii (D12, D13). Uruchomienie: python -m unittest tools/test_bib2bibitem.py"""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bib2bibitem import collect_cites, format_authors, format_entry, parse_bib, unique, uporzadkuj  # noqa: E402

BIB = r"""
@article{zeta2020,
  author = {Zeta, Anna and Beta, Bob},
  title = {Ostatni alfabetycznie},
  journal = {Journal Z}, volume = {1}, pages = {1--10}, year = {2020},
  doi = {10.1000/z}, status = {Z}, dostep = {A}, rozdzial = {1.1}, weryfikacja = {TAJNA-NOTATKA}
}
@book{astrom2021,
  author = {{\AA}str{\"o}m, Karl Johan and Murray, Richard M.},
  title = {Feedback Systems}, publisher = {Princeton University Press}, year = {2021},
  url = {https://example.org/fbs.pdf}, urldate = {2026-10-08}, dostep = {B}
}
@inproceedings{atil2025,
  author = {At{\i}l, Berk and Aykent, Sarp and Chittams, Alexa and Fu, Lisheng},
  title = {Non-Determinism of ``Deterministic'' Settings},
  booktitle = {Eval4NLP 2025}, pages = {135--148}, year = {2025},
  doi = {10.18653/v1/x}, dostep = {A}
}
@article{beta2019,
  author = {Beta, Bob and Gamma, Carl and Delta, Dan},
  title = {Trzech autorów}, journal = {J}, year = {2019},
  doi = {10.1000/b_1}, url = {https://repo.example.org/b.pdf}, urldate = {2026-10-08},
  urlwersja = {preprint}, dostep = {B}
}
@article{gamma2018,
  author = {Gamma, Carl and others},
  title = {Zamknięty}, journal = {J}, year = {2018}, doi = {10.1000/c}, dostep = {C}
}
@misc{eps2024,
  author = {Eps, Ela}, title = {Preprint}, year = {2024},
  eprint = {2401.00001v2}, archiveprefix = {arXiv}, dostep = {A}
}
@book{kappa2016,
  author = {Kappa, Kim}, title = {Podręcznik}, publisher = {Academic Press}, year = {2016},
  url = {https://example.org/katalog}, dostep = {C}
}
"""


def wpisy():
    e = parse_bib(BIB)
    order = e.pop("__order__")
    return e, order


class TestKolejnosc(unittest.TestCase):
    def test_alfabetyczna(self):
        e, order = wpisy()
        # Åström pod „A”, Atıl po Åström („astrom” < „atil”), Zeta na końcu
        self.assertEqual(uporzadkuj(order, e, "alfabetyczna"),
                         ["astrom2021", "atil2025", "beta2019", "eps2024", "gamma2018", "kappa2016", "zeta2020"])

    def test_cytowania(self):
        e, _ = wpisy()
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "rozdz.tex").write_text(r"Dalej~\cite{zeta2020, atil2025}.", encoding="utf-8")
            (Path(d) / "main.tex").write_text("Najpierw~\\cite{gamma2018}.\n\\input{rozdz}\n% \\cite{beta2019}\n\\cite[s.~5]{gamma2018}",
                                              encoding="utf-8")
            keys = unique(collect_cites(Path(d) / "main.tex"))
        self.assertEqual(uporzadkuj(keys, e, "cytowania"), ["gamma2018", "zeta2020", "atil2025"])


class TestAutorzy(unittest.TestCase):
    def test_do_trzech_wszyscy(self):
        self.assertEqual(format_authors("Beta, Bob and Gamma, Carl and Delta, Dan"), "B.~Beta, C.~Gamma, D.~Delta")

    def test_powyzej_trzech_i_in(self):
        self.assertEqual(format_authors("At{\\i}l, Berk and Aykent, Sarp and Chittams, Alexa and Fu, Lisheng"), "B.~Atıl i~in.")

    def test_others_i_in(self):
        self.assertEqual(format_authors("Gamma, Carl and others"), "C.~Gamma i~in.")

    def test_znaki_specjalne(self):
        self.assertEqual(format_authors("{\\AA}str{\\\"o}m, Karl Johan"), "K.~J.~Åström")


class TestOdnosniki(unittest.TestCase):
    def test_kategoria_A_doi(self):
        e, _ = wpisy()
        s = format_entry(e["zeta2020"], dostep="2026-10-08")
        self.assertTrue(s.endswith(" Dostępne online: \\url{https://doi.org/10.1000/z} [dostęp: 08.10.2026]."), s)

    def test_kategoria_A_preprint_arxiv_z_wersja(self):
        e, _ = wpisy()
        s = format_entry(e["eps2024"], dostep="2026-10-08")
        self.assertIn("preprint arXiv:2401.00001v2", s)
        self.assertIn("\\url{https://arxiv.org/abs/2401.00001v2} [dostęp: 08.10.2026]", s)

    def test_kategoria_B_doi_i_kopia(self):
        e, _ = wpisy()
        s = format_entry(e["beta2019"], dostep="2000-01-01")
        self.assertIn(" DOI: 10.1000/b\\_1.", s)
        self.assertIn(" Dostępne online (preprint): \\url{https://repo.example.org/b.pdf} [dostęp: 08.10.2026].", s)

    def test_kategoria_B_bez_doi(self):
        e, _ = wpisy()
        s = format_entry(e["astrom2021"], dostep="2026-10-08")
        self.assertNotIn("DOI", s)
        self.assertTrue(s.endswith("Dostępne online: \\url{https://example.org/fbs.pdf} [dostęp: 08.10.2026]."), s)

    def test_kategoria_C_tylko_doi(self):
        # D16: pozycja płatna z DOI: „DOI: …” bez „Dostępne online” i daty dostępu
        e, _ = wpisy()
        s = format_entry(e["gamma2018"], dostep="2026-10-08")
        self.assertTrue(s.endswith(", 2018. DOI: 10.1000/c."), s)
        self.assertNotIn("Dostępne online", s)
        self.assertNotIn("dostęp:", s)

    def test_kategoria_C_bez_doi_bez_odnosnika(self):
        e, _ = wpisy()
        s = format_entry(e["kappa2016"], dostep="2026-10-08")
        self.assertNotIn("DOI", s)
        self.assertNotIn("Dostępne online", s)
        self.assertNotIn("example.org", s)

    def test_pola_wlasne_poza_wynikiem(self):
        e, _ = wpisy()
        s = format_entry(e["zeta2020"], dostep="2026-10-08")
        for x in ("TAJNA-NOTATKA", "1.1", "status", "dostep"):
            self.assertNotIn(x, s)

    def test_cudzyslow_zagniezdzony(self):
        e, _ = wpisy()
        self.assertIn("„Non-Determinism of «Deterministic» Settings”", format_entry(e["atil2025"], dostep="2026-10-08"))


if __name__ == "__main__":
    unittest.main()
