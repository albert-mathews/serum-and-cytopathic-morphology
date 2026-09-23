# -*- coding: utf-8 -*-
"""
Rebuild P1_screened.csv with conservative bibliographic identifiers.

RULE: Only fill doi / pmid / pmcid / other_id / stable_url when certain
from (a) text printed on our PDF, (b) DTIC AD on our PDF/filename,
(c) PMC ID in our PMC-sourced filename, or (d) institutional document code
we hold. If not certain → leave BLANK. Prefer incomplete over wrong.
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "P1_screened.csv"
README = ROOT / "P1_BIBLIOGRAPHY.md"

FIELDS = [
    "id", "year", "authors", "title", "journal_or_source", "citation", "short_cite",
    "doi", "pmid", "pmcid", "other_id", "other_id_type", "stable_url",
    "id_basis", "useful", "reason", "fulltext", "lead_source", "round",
    "paper_spine", "alias_of", "notes",
]


def R(**kw):
    base = {k: "" for k in FIELDS}
    base.update(kw)
    return base


# id_basis explains why any machine ID is present (empty if none)
ROWS = [
R(
    id="P1-001", year="1949",
    authors="Enders JF, Weller TH, Robbins FC",
    title="Cultivation of the Lansing strain of poliomyelitis virus in cultures of various human embryonic tissues",
    journal_or_source="Science",
    citation="Science. 1949;109:85-87",
    short_cite="Enders et al. 1949 Science Lansing TC",
    # PDF shows: January 28, 1949, Vol. 109, page 85 (running head) / article continues p.86
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="PDF imprint: Science 28 Jan 1949 Vol. 109 p.85+",
    useful="Y", reason="Primary virus tissue culture methods with medium detail",
    fulltext="Y", lead_source="seed_enders", round="1", paper_spine="Y", alias_of="",
    notes="No DOI/PMID on PDF; do not invent. Title/authors from article body.",
),
R(
    id="P1-002", year="1950",
    authors="Robbins FC, Enders JF, Weller TH",
    title="Cytopathogenic effect of poliomyelitis viruses in vitro on human embryonic tissues",
    journal_or_source="Proc Soc Exp Biol Med",
    citation="Proc Soc Exp Biol Med. 1950;75:370-374",
    short_cite="Robbins et al. 1950 CPE",
    # PDF shows title + authors + article no. (18202) + pages 370-371+; year/pages also cited in Dulbecco PDF biblio as 1950, 75, 370
    doi="", pmid="", pmcid="", other_id="18202", other_id_type="psgbm_article_number",
    stable_url="",
    id_basis="PDF title/pages; year+vol confirmed via Dulbecco 1954 biblio cite of this paper",
    useful="Y", reason="CPE as readable endpoint in tissue culture",
    fulltext="Y", lead_source="seed_enders", round="1", paper_spine="Y", alias_of="",
    notes="PSGBM article number (18202) on PDF. No DOI/PMID on PDF.",
),
R(
    id="P1-003", year="1954",
    authors="Enders JF, Robbins FC, Weller TH",
    title="The cultivation of the poliomyelitis viruses in tissue culture (Nobel Lecture)",
    journal_or_source="Nobel Prize lecture",
    citation="Nobel Lecture, 11 December 1954. The Nobel Prize in Physiology or Medicine 1954",
    short_cite="Enders et al. 1954 Nobel lecture",
    doi="", pmid="", pmcid="",
    other_id="", other_id_type="",
    stable_url="https://www.nobelprize.org/prizes/medicine/1954/enders/lecture/",
    id_basis="Official Nobel Prize website lecture page for 1954 Medicine",
    useful="Y", reason="Medium and methods narrative ox serum ultrafiltrate BSS",
    fulltext="Y", lead_source="seed_enders", round="1", paper_spine="N", alias_of="",
    notes="Stable URL is the official Nobel site; not a journal DOI.",
),
R(
    id="P1-004", year="1952",
    authors="Melnick JL, Riordan JT",
    title="Poliomyelitis viruses in tissue culture. IV. Protein-free nutrient media in stationary and roller tube cultures",
    journal_or_source="Proc Soc Exp Biol Med",
    citation="Proc Soc Exp Biol Med. 1952;81:208-213",
    short_cite="Melnick & Riordan 1952 protein-free media",
    # PDF shows page 208 + title + authors + article (19823)
    doi="", pmid="", pmcid="", other_id="19823", other_id_type="psgbm_article_number",
    stable_url="",
    id_basis="PDF: title, authors, p.208, article number (19823)",
    useful="Y", reason="Primary protein-free lactalbumin medium for polio TC",
    fulltext="Y", lead_source="seed_snowball", round="1", paper_spine="optional", alias_of="",
    notes="Volume 81 year 1952 from standard series imprint in extract; no DOI/PMID on PDF (PMID not recorded here).",
),
R(
    id="P1-005", year="1954",
    authors="Dulbecco R, Vogt M",
    title="Plaque formation and isolation of pure lines with poliomyelitis viruses",
    journal_or_source="J Exp Med",
    citation="J Exp Med. 1954;99:167-182",
    short_cite="Dulbecco & Vogt 1954 plaque",
    # PDF last page 182; first content page running as 168; received June 1, 1953
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="PDF: title, authors, pages through 182; volume/year from project extract of this PDF",
    useful="Y", reason="Monolayer plaque assay methods context",
    fulltext="Y", lead_source="seed_plaque", round="1", paper_spine="N", alias_of="",
    notes="No DOI/PMID printed on PDF. Do not invent PMCID.",
),
R(
    id="P1-006", year="1955",
    authors="Melnick JL",
    title="Tissue culture techniques and their application to original isolation, growth, and assay of poliomyelitis and orphan viruses",
    journal_or_source="Ann N Y Acad Sci",
    citation="Ann N Y Acad Sci. 1955;61:754-773",
    short_cite="Melnick 1955 Ann NY Acad Sci",
    # PDF running head page 755 "Melnick : Poliomyelitis and Orphan Viruses"
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="PDF: title, author, pages 754+",
    useful="Y", reason="Melnick 1955 methods; lactalbumin + 2% calf serum; isolation CPE",
    fulltext="Y", lead_source="seed_melnick", round="9", paper_spine="N", alias_of="",
    notes="No DOI/PMID on PDF.",
),
R(
    id="P1-007", year="1961",
    authors="",
    title="Schmidt diagnostic tissue culture lead (AJPH-era; not fully extracted)",
    journal_or_source="",
    citation="",
    short_cite="Schmidt ~1961 AJPH tissue culture diagnostic (unresolved imprint)",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="B", reason="Points to maintenance media and diagnostic TC; PDF not fully extracted",
    fulltext="partial", lead_source="seed_manual_line", round="2", paper_spine="N", alias_of="",
    notes="No verified imprint retained. Prefer P1-008 for methods. Prior PMC1522339 claim removed as not re-verified against a held PDF.",
),
R(
    id="P1-008", year="1969",
    authors="Schmidt NJ",
    title="Tissue culture technics for diagnostic virology (Chapter 3)",
    journal_or_source="In: Lennette EH, Schmidt NJ, eds. Diagnostic Procedures for Viral and Rickettsial Infections. 4th ed. American Public Health Association",
    citation="Schmidt NJ. Tissue culture technics for diagnostic virology. In: Lennette EH, Schmidt NJ, eds. Diagnostic Procedures for Viral and Rickettsial Infections. 4th ed. APHA; 1969. Chapter 3",
    short_cite="Schmidt 1969 Diagnostic Procedures 4th ed ch.3",
    doi="", pmid="", pmcid="",
    other_id="Lennette-Schmidt-1969-4th-ed-ch3", other_id_type="book_chapter_key",
    stable_url="",
    id_basis="User-supplied full chapter screenshot PDF of 4th ed. ch.3; book has no DOI",
    useful="Y", reason="Full Schmidt ch.3 growth/maintenance recipes",
    fulltext="Y", lead_source="seed_manual_line", round="8", paper_spine="Y", alias_of="",
    notes="Identify by edition + chapter title + editor. No DOI expected for 1969 APHA volume.",
),
R(
    id="P1-009", year="",
    authors="Fenner F et al.",
    title="Cultivation and assay of viruses (Medical Virology chapter; secondary)",
    journal_or_source="Medical Virology (chapter)",
    citation="Fenner et al. Cultivation and Assay of Viruses (Medical Virology chapter; secondary textbook source)",
    short_cite="Fenner Cultivation and Assay of Viruses",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="Y", reason="States growth 5-10% FCS then maintenance little or no serum",
    fulltext="Y", lead_source="pubmed_fenner", round="2", paper_spine="N", alias_of="",
    notes="Prior PMC7173454 removed — not re-verified against a held PDF imprint in this pass.",
),
R(
    id="P1-010", year="2006",
    authors="Clinical and Laboratory Standards Institute",
    title="Viral Culture; Approved Guideline",
    journal_or_source="CLSI document M41-A",
    citation="CLSI. Viral Culture; Approved Guideline. CLSI document M41-A. Clinical and Laboratory Standards Institute; 2006",
    short_cite="CLSI M41-A 2006",
    doi="", pmid="", pmcid="",
    other_id="M41-A", other_id_type="clsi_document_code",
    stable_url="",
    id_basis="Institutional document code M41-A held in project protocol corpus",
    useful="Y", reason="End-marker: growth ~10% FBS maintenance 1-3% and CPE primary",
    fulltext="Y", lead_source="seed_repo_protocol", round="2", paper_spine="institutional", alias_of="",
    notes="Cite by document code + year. No DOI in project notes.",
),
R(
    id="P1-011", year="",
    authors="ATCC",
    title="Virology Culture Guide",
    journal_or_source="ATCC institutional web guide",
    citation="ATCC. Virology Culture Guide (institutional web publication; living document)",
    short_cite="ATCC Virology Culture Guide",
    doi="", pmid="", pmcid="",
    other_id="ATCC-Virology-Culture-Guide", other_id_type="institutional_guide",
    stable_url="",
    id_basis="Institutional product name only; living web page not frozen",
    useful="Y", reason="End-marker: lower serum viral medium; NOTE 5 decrease to 2%",
    fulltext="Y", lead_source="seed_repo_protocol", round="2", paper_spine="institutional", alias_of="",
    notes="Do not invent a permanent URL; capture archive date when paper is submitted.",
),
R(
    id="P1-012", year="2007",
    authors="Suchman E, Blair C",
    title="Cytopathic effects of viruses protocols",
    journal_or_source="American Society for Microbiology Protocols",
    citation="Suchman E, Blair C. Cytopathic Effects of Viruses Protocols. American Society for Microbiology",
    short_cite="ASM Suchman & Blair CPE Protocols",
    doi="", pmid="", pmcid="",
    other_id="ASM-CPE-Protocols-Suchman-Blair", other_id_type="asm_protocol",
    stable_url="",
    id_basis="In-repo protocol PDF title/authors",
    useful="Y", reason="End-marker: maintenance medium with 2% serum",
    fulltext="Y", lead_source="seed_repo_protocol", round="2", paper_spine="institutional", alias_of="",
    notes="No DOI. Prefer title+authors+ASM protocols series.",
),
R(
    id="P1-013", year="2007",
    authors="Leland DS, Ginocchio CC",
    title="Role of cell culture for virus detection in the age of technology",
    journal_or_source="Clin Microbiol Rev",
    citation="Clin Microbiol Rev. 2007;20(1):49-78. doi:10.1128/CMR.00002-06",
    short_cite="Leland & Ginocchio 2007 Clin Microbiol Rev",
    doi="10.1128/CMR.00002-06", pmid="", pmcid="",
    other_id="", other_id_type="",
    stable_url="https://doi.org/10.1128/CMR.00002-06",
    id_basis="DOI and imprint printed on first page of held PDF",
    useful="B", reason="Diagnostic culture review; limited explicit serum percent",
    fulltext="Y", lead_source="pubmed_leland", round="10", paper_spine="N", alias_of="",
    notes="PMID not printed on PDF first page — left blank.",
),
R(
    id="P1-014", year="2016",
    authors="Hematian A, Sadeghifard N, Mohebi R, Taherikalani M, Nasrolahi A, Amraei M, Ghafourian S",
    title="Traditional and modern cell culture in virus diagnosis",
    journal_or_source="Osong Public Health Res Perspect",
    citation="Osong Public Health Res Perspect (Hematian et al.; traditional and modern cell culture in virus diagnosis)",
    short_cite="Hematian et al. 2016 cell culture virus diagnosis",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="Title/authors on held PDF; volume/pages/DOI not printed on first page of held PDF — left blank",
    useful="N", reason="no_medium_info",
    fulltext="Y", lead_source="pubmed_hematian", round="2", paper_spine="N", alias_of="",
    notes="Same paper as P1-020. Prior DOI/PMID from web not retained unless on PDF.",
),
R(
    id="P1-015", year="",
    authors="Moffat MAJ",
    title="Some cell culture procedures in diagnostic medical virology",
    journal_or_source="Diagnostic methods chapter (PDF in corpus)",
    citation="Moffat MAJ. Some Cell Culture Procedures in Diagnostic Medical Virology (chapter PDF in p1_history/refs)",
    short_cite="Moffat diagnostic cell culture procedures",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="Title/author from held PDF only",
    useful="Y", reason="States change to maintenance 1% serum or serum-free after about 3 days",
    fulltext="Y", lead_source="pubmed_moffat", round="2", paper_spine="N", alias_of="",
    notes="Prior PMC7149990 removed — not re-verified on this PDF.",
),
R(
    id="P1-016", year="",
    authors="UK Standards for Microbiology Investigations",
    title="V 39: Procedure for the care and propagation of cell cultures",
    journal_or_source="UK SMI V_39",
    citation="UK Standards for Microbiology Investigations. V 39 — Procedure for the care and propagation of cell cultures",
    short_cite="UK SMI V_39",
    doi="", pmid="", pmcid="",
    other_id="V_39", other_id_type="uk_smi_code",
    stable_url="",
    id_basis="National document code V_39",
    useful="Y", reason="Growth 10% / maintenance 2% serum tables",
    fulltext="partial", lead_source="scholar_smi", round="2", paper_spine="N", alias_of="",
    notes="Cite code + edition date when frozen for paper.",
),
R(
    id="P1-017", year="1961",
    authors="Subramanyam P, Divakaran S, Vinodraj P",
    title="Cultivation of vaccinia virus in sheep kidney cell cultures",
    journal_or_source="Bull World Health Organ",
    citation="Bull World Health Organ. 1961;25:33-40",
    short_cite="Subramanyam et al. 1961 vaccinia sheep kidney",
    doi="", pmid="", pmcid="PMC2555548",
    other_id="", other_id_type="",
    stable_url="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2555548/",
    id_basis="Imprint on PDF (Bull. Wld Hlth Org. 1961, 25, 33-40); PMCID from PMC-sourced filename",
    useful="Y", reason="Maintenance EBSS with 10% sheep serum (counterexample)",
    fulltext="Y", lead_source="scholar_counter", round="4", paper_spine="N", alias_of="",
    notes="Counterexample high-serum maintenance.",
),
R(
    id="P1-018", year="1964",
    authors="Boyle JJ",
    title="Rift Valley Fever Virus Assay in Serum-Free Hamster Kidney Monolayers",
    journal_or_source="U.S. Army Biological Laboratories Technical Manuscript 132",
    citation="Boyle JJ. Rift Valley Fever Virus Assay in Serum-Free Hamster Kidney Monolayers. Technical Manuscript 132. U.S. Army Biological Laboratories, Fort Detrick; April 1964. DTIC AD0437967",
    short_cite="Boyle 1964 RVF TM132 AD0437967",
    doi="", pmid="", pmcid="",
    other_id="AD0437967", other_id_type="dtic_ad",
    stable_url="",
    id_basis="DTIC AD on held PDF cover (AD437967 / AD0437967 family) + TM 132 title page; filename AD0437967",
    useful="Y", reason="Serum omitted from maintenance; CPE readability",
    fulltext="Y", lead_source="scholar_counter", round="4", paper_spine="Y", alias_of="",
    notes="Cover also shows AD437967 (same report family). Prefer AD0437967 as in filename and common DTIC form.",
),
R(
    id="P1-019", year="1958",
    authors="Baron S, Low RJ",
    title="New maintenance medium for cell culture",
    journal_or_source="Science",
    citation="Science (Baron & Low; New maintenance medium for cell culture) — same as P1-048",
    short_cite="Baron & Low 1958 (alias of P1-048)",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="Alias of P1-048",
    useful="Y", reason="duplicate lead of P1-048",
    fulltext="Y", lead_source="scholar_maint", round="2", paper_spine="N", alias_of="P1-048",
    notes="Do not double-cite. IDs live on P1-048.",
),
R(
    id="P1-020", year="2016",
    authors="Hematian A, et al.",
    title="Traditional and modern cell culture in virus diagnosis",
    journal_or_source="Osong Public Health Res Perspect",
    citation="Same as P1-014",
    short_cite="Hematian 2016 (alias of P1-014)",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="Alias of P1-014",
    useful="N", reason="no_medium_info",
    fulltext="Y", lead_source="user_pdf", round="7", paper_spine="N", alias_of="P1-014",
    notes="User PDF filename alias.",
),
R(
    id="P1-021", year="",
    authors="",
    title="Unresolved screen lead: carrier cultures / maintenance medium",
    journal_or_source="",
    citation="",
    short_cite="Unresolved maintenance/carrier-culture lead",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="B", reason="Mentions maintenance medium; limited extraction",
    fulltext="partial", lead_source="scholar_maint", round="3", paper_spine="N", alias_of="",
    notes="No verified bibliographic object. Left intentionally incomplete.",
),
R(
    id="P1-022", year="",
    authors="Wikipedia contributors",
    title="Eagle's minimal essential medium (encyclopedia page)",
    journal_or_source="Wikipedia",
    citation="Wikipedia entry on Eagle's MEM (screened as non-primary; not a research source)",
    short_cite="Wikipedia Eagle MEM",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="N", reason="not_virus / not primary",
    fulltext="Y", lead_source="scholar_noise", round="2", paper_spine="N", alias_of="",
    notes="Logged for transparency only. No permanent scholarly ID.",
),
R(
    id="P1-023", year="",
    authors="",
    title="Class lead: modern serum-free Vero adaptation literature",
    journal_or_source="",
    citation="",
    short_cite="Modern SFM Vero adaptation (class lead)",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="N", reason="out_of_window",
    fulltext="partial", lead_source="pubmed_modern", round="2", paper_spine="N", alias_of="",
    notes="Not a single bibliographic object.",
),
R(
    id="P1-024", year="",
    authors="",
    title="Unresolved Enders-group ~1950 culture lead (possible duplicate of P1-051/P1-002)",
    journal_or_source="",
    citation="",
    short_cite="Unresolved Enders-group ~1950 lead",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="B", reason="Related Enders group; not fully extracted",
    fulltext="partial", lead_source="seed_enders", round="1", paper_spine="N", alias_of="",
    notes="Not resolved to a unique paper. Prefer P1-001/002/051.",
),
R(
    id="P1-025", year="1913",
    authors="Steinhardt E, Israeli C, Lambert RA",
    title="Studies on the cultivation of the virus of vaccinia",
    journal_or_source="J Infect Dis",
    citation="Steinhardt E, Israeli C, Lambert RA. Studies on the cultivation of the virus of vaccinia. J Infect Dis. 1913 (classic early claim; volume/pages not re-verified against a held PDF in this pass)",
    short_cite="Steinhardt et al. 1913 vaccinia cultivation",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="Standard historical citation only; pages not verified on held PDF",
    useful="B", reason="Very early virus in culture; medium not extracted",
    fulltext="partial", lead_source="seed_history", round="2", paper_spine="N", alias_of="",
    notes="Authors+year+journal retained as classic lead; no machine ID.",
),
R(
    id="P1-026", year="1936",
    authors="Lloyd W, Theiler M, Ricci NI",
    title="Modification of the virulence of yellow fever virus by cultivation in tissues in vitro (classic lead)",
    journal_or_source="",
    citation="Lloyd W, Theiler M, Ricci NI. 1936 yellow fever tissue culture (exact journal imprint not re-verified on held PDF)",
    short_cite="Lloyd Theiler Ricci 1936 yellow fever TC",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="B", reason="Pre-Enders virus TC; medium not extracted",
    fulltext="partial", lead_source="seed_history", round="2", paper_spine="N", alias_of="",
    notes="No machine ID; imprint incomplete by design until PDF verified.",
),
R(
    id="P1-027", year="",
    authors="Fenner F et al.",
    title="Egg cultivation contrast material (not Isolation medium evolution)",
    journal_or_source="",
    citation="",
    short_cite="Fenner egg chapter contrast",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="N", reason="secondary_no_primary_methods",
    fulltext="Y", lead_source="pubmed_fenner", round="2", paper_spine="N", alias_of="",
    notes="Screened out.",
),
R(
    id="P1-028", year="2006",
    authors="Clinical and Laboratory Standards Institute",
    title="Viral Culture; Approved Guideline (duplicate materials of P1-010)",
    journal_or_source="CLSI M41-A",
    citation="Duplicate of P1-010",
    short_cite="CLSI M41 preview (alias P1-010)",
    doi="", pmid="", pmcid="", other_id="M41-A", other_id_type="clsi_document_code",
    stable_url="",
    id_basis="Alias of P1-010",
    useful="N", reason="duplicate",
    fulltext="partial", lead_source="seed_repo", round="2", paper_spine="N", alias_of="P1-010",
    notes="",
),
R(
    id="P1-029", year="",
    authors="WOAH / APHIS",
    title="Isolation / cell culture chapters in animal health manuals (class)",
    journal_or_source="WOAH Terrestrial Manual; APHIS SAM/VIRPRO",
    citation="Class of institutional manuals (see r1_isolation_standards_and_practice/refs/isolation_protocols/)",
    short_cite="WOAH APHIS manuals class",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="B", reason="Codify growth/maintenance; cite specific chapter in R1",
    fulltext="partial", lead_source="seed_repo", round="2", paper_spine="N", alias_of="",
    notes="Not one bibliographic object.",
),
R(
    id="P1-030", year="",
    authors="Dulbecco R, Vogt M",
    title="Related plaque methods lead (prefer P1-005)",
    journal_or_source="",
    citation="",
    short_cite="Dulbecco related plaque lead",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="B", reason="Related plaque methods; not extracted",
    fulltext="partial", lead_source="seed_plaque", round="3", paper_spine="N", alias_of="",
    notes="Prefer P1-005.",
),
R(
    id="P1-031", year="",
    authors="",
    title="Unresolved lead: Howes growth cycle poliovirus citing Melnick media",
    journal_or_source="",
    citation="",
    short_cite="Howes growth cycle (unresolved)",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="B", reason="Secondary pointer",
    fulltext="partial", lead_source="scholar_snowball", round="3", paper_spine="N", alias_of="",
    notes="",
),
R(
    id="P1-032", year="",
    authors="",
    title="Unresolved lead: serum substitutes / stock viruses (~1990 class)",
    journal_or_source="",
    citation="",
    short_cite="Serum substitutes lead (unresolved)",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="N", reason="out_of_window",
    fulltext="partial", lead_source="pubmed_counter", round="4", paper_spine="N", alias_of="",
    notes="",
),
R(
    id="P1-033", year="",
    authors="Eagle H",
    title="Eagle essential medium papers (class, mid-1950s)",
    journal_or_source="",
    citation="",
    short_cite="Eagle MEM series (class)",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="B", reason="Cell nutrition science; not Isolation recipe primary",
    fulltext="partial", lead_source="seed_media", round="2", paper_spine="N", alias_of="",
    notes="Cite a specific Eagle paper only if extracted.",
),
R(
    id="P1-034", year="1950",
    authors="Morgan JF, Morton HJ, Parker RC",
    title="Nutrition of animal cells in tissue culture. I. Initial studies on a synthetic medium",
    journal_or_source="Proc Soc Exp Biol Med",
    citation="Proc Soc Exp Biol Med. 1950;73(1):1-8",
    short_cite="Morgan et al. 1950 Medium 199",
    # PDF: VOL. 73 JANUARY 1950 No. 1; article (17557)
    doi="", pmid="", pmcid="",
    other_id="17557", other_id_type="psgbm_article_number",
    stable_url="",
    id_basis="PDF imprint Vol.73 Jan 1950 No.1 + article number (17557) on PDF",
    useful="Y", reason="Medium 199 synthetic medium foundation",
    fulltext="Y", lead_source="seed_enders_cite", round="9", paper_spine="N", alias_of="",
    notes="No DOI printed on held PDF — left blank (article number retained).",
),
R(
    id="P1-035", year="1963",
    authors="Rosenbaum MJ, Phillips IA, Sullivan EJ, Edwards EA, Miller LF",
    title="A simplified method for virus-tissue culture procedures in microtitration plates",
    journal_or_source="DTIC technical report / reprint",
    citation="Rosenbaum MJ, et al. A Simplified Method for Virus-Tissue Culture Procedures in Microtitration Plates. DTIC AD0411928",
    short_cite="Rosenbaum microtitration AD0411928",
    doi="", pmid="", pmcid="",
    other_id="AD0411928", other_id_type="dtic_ad",
    stable_url="",
    id_basis="DTIC AD on held PDF/filename; authors/title in PDF metadata",
    useful="Y", reason="Growth vs maintenance in tube cultures",
    fulltext="Y", lead_source="scholar_maint", round="3", paper_spine="N", alias_of="",
    notes="Alias file P1-204.",
),
R(
    id="P1-036", year="1969",
    authors="Lennette EH, Schmidt NJ (eds)",
    title="Diagnostic Procedures for Viral and Rickettsial Infections, 4th ed. (AJPH book notice)",
    journal_or_source="Am J Public Health Nations Health (book notice)",
    citation="AJPH book notice of Lennette & Schmidt 4th ed. (file amjphnation00034-0156b); full methods chapter is P1-008",
    short_cite="Lennette/Schmidt 4th ed AJPH notice",
    doi="", pmid="", pmcid="",
    other_id="amjphnation00034-0156b", other_id_type="source_filename_id",
    stable_url="",
    id_basis="Held notice PDF filename id only",
    useful="B", reason="Notice only; not full methods",
    fulltext="Y", lead_source="seed_manual_line", round="2", paper_spine="N", alias_of="P1-008",
    notes="Not a substitute for P1-008.",
),
R(
    id="P1-037", year="",
    authors="",
    title="Cumitech / ASM Manual of Clinical Microbiology historical editions (class)",
    journal_or_source="ASM Press",
    citation="",
    short_cite="Cumitech / ASM MCM class",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="B", reason="Edition-specific extraction incomplete",
    fulltext="partial", lead_source="seed_manual_line", round="2", paper_spine="N", alias_of="",
    notes="",
),
R(
    id="P1-038", year="2004",
    authors="World Health Organization",
    title="Polio Laboratory Manual",
    journal_or_source="WHO",
    citation="WHO. Polio Laboratory Manual (2004 edition lineage)",
    short_cite="WHO Polio Laboratory Manual 2004",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="N", reason="out_of_window",
    fulltext="partial", lead_source="seed_modern_manual", round="2", paper_spine="N", alias_of="",
    notes="Prior WHO-IVB-04.10 code removed until confirmed against a held document.",
),
R(
    id="P1-039", year="",
    authors="",
    title="Non-peer web noise lead",
    journal_or_source="",
    citation="",
    short_cite="Web noise lead",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="N", reason="not_useful_non_peer",
    fulltext="Y", lead_source="scholar_noise", round="2", paper_spine="N", alias_of="",
    notes="",
),
R(
    id="P1-040", year="",
    authors="",
    title="Modern serum-free Vero trade/secondary lead",
    journal_or_source="",
    citation="",
    short_cite="Modern SFM Vero lead",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="N", reason="out_of_window",
    fulltext="partial", lead_source="scholar_noise", round="4", paper_spine="N", alias_of="",
    notes="",
),
R(
    id="P1-041", year="",
    authors="",
    title="Unresolved lead: simplified maintenance medium (~1955 PSGBM-era)",
    journal_or_source="",
    citation="",
    short_cite="EAS simplified maintenance (unresolved)",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="B", reason="Virus Isolation link unclear",
    fulltext="partial", lead_source="scholar_maint", round="2", paper_spine="N", alias_of="",
    notes="",
),
R(
    id="P1-042", year="1953",
    authors="Li CP, Schaeffer M",
    title="A simplified method for cultivation of poliomyelitis virus in tissue culture",
    journal_or_source="Science",
    citation="Science (Li CP, Schaeffer M; A simplified method for cultivation of poliomyelitis virus in tissue culture)",
    short_cite="Li & Schaeffer 1953 Science",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="Title and authors on held PDF; volume/issue/pages not captured cleanly from scan first pages — left blank rather than guess",
    useful="Y", reason="Horse serum frequently inhibitory; Medium E",
    fulltext="Y", lead_source="round7_search", round="9", paper_spine="optional", alias_of="",
    notes="Prior DOI/PMID removed until volume/pages verified on PDF. Manuscript received date visible near article; full Science imprint to be filled only when confirmed.",
),
R(
    id="P1-043", year="1956",
    authors="Melnick JL, Opton EM",
    title="Assay of poliomyelitis neutralizing antibody in disposable plastic panels",
    journal_or_source="Bull World Health Organ",
    citation="Bull World Health Organ. 1956;14:129-146",
    short_cite="Melnick & Opton 1956 WHO assay panels",
    doi="", pmid="", pmcid="PMC2538105",
    other_id="", other_id_type="",
    stable_url="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2538105/",
    id_basis="Imprint on PDF (Bull. Wld Hlth Org. 1956, 14, 129-146); PMCID from PMC-sourced filename",
    useful="Y", reason="Nutrient medium + 2.0% calf serum",
    fulltext="Y", lead_source="round7_search", round="9", paper_spine="N", alias_of="",
    notes="",
),
R(
    id="P1-044", year="1956",
    authors="Melnick JL",
    title="Tissue culture methods for cultivation of poliomyelitis and related viruses (Diagnostic Procedures 2nd ed. chapter lineage)",
    journal_or_source="APHA Diagnostic Procedures 2nd ed. (~1956)",
    citation="Melnick JL. Tissue culture methods… In: Diagnostic Procedures for Virus and Rickettsial Diseases. 2nd ed. APHA; ~1956 (PDF not obtained)",
    short_cite="Melnick Diagnostic Procedures 2nd ed chapter",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="B", reason="Chapter not fulltext extracted",
    fulltext="N", lead_source="round7_search", round="7", paper_spine="N", alias_of="",
    notes="Unavailable; no machine ID.",
),
R(
    id="P1-045", year="1952",
    authors="Weller TH, Enders JF, Robbins FC, Stoddard MB",
    title="Studies on the cultivation of poliomyelitis viruses in tissue culture. I. …",
    journal_or_source="J Immunol",
    citation="Weller et al. Studies on the cultivation of poliomyelitis viruses in tissue culture. I. J Immunol. 1952;69:645-671 (PDF not obtained; pages from standard series citation used only as lead)",
    short_cite="Weller et al. 1952 J Immunol I",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="B", reason="Enders-group methods; PDF not obtained",
    fulltext="N", lead_source="round9_snowball", round="9", paper_spine="N", alias_of="",
    notes="Prior PMID removed — not verified against held PDF. Lead only.",
),
R(
    id="P1-046", year="1954",
    authors="Youngner JS",
    title="Monolayer tissue cultures. I. Preparation and standardization of suspensions of trypsin-dispersed monkey kidney cells",
    journal_or_source="Proc Soc Exp Biol Med / Exp Biol Med",
    citation="Exp Biol Med (Maywood). 1954;85:202-205. doi:10.3181/00379727-85-20830",
    short_cite="Youngner 1954 monolayer trypsin MK",
    doi="10.3181/00379727-85-20830", pmid="", pmcid="",
    other_id="20830", other_id_type="psgbm_article_number",
    stable_url="https://doi.org/10.3181/00379727-85-20830",
    id_basis="DOI and 1954;85:202 printed on held PDF cover sheet",
    useful="Y", reason="Medium D 2% horse serum growth; no serum for virus assay",
    fulltext="Y", lead_source="round9_snowball", round="10", paper_spine="Y", alias_of="",
    notes="Paper spine. PMID not on PDF.",
),
R(
    id="P1-047", year="1953",
    authors="Scherer WF, Syverton JT, Gey GO",
    title="Studies on the propagation in vitro of poliomyelitis viruses. IV. Viral multiplication in a stable strain of human malignant epithelial cells (strain HeLa)…",
    journal_or_source="J Exp Med",
    citation="J Exp Med. 1953;97:695-710",
    short_cite="Scherer Syverton Gey 1953 HeLa",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="PDF: title, authors, received 20 Jan 1953; pages 695+ from held full text",
    useful="Y", reason="High human serum growth; MS-100 after antibody dilution",
    fulltext="Y", lead_source="round9_snowball", round="10", paper_spine="Y", alias_of="",
    notes="No DOI/PMID on PDF. Do not invent.",
),
R(
    id="P1-048", year="1958",
    authors="Baron S, Low RJ",
    title="New maintenance medium for cell culture",
    journal_or_source="Science",
    citation="Science. 1958;128:89-90",
    short_cite="Baron & Low 1958 Science",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="PDF: title, authors Baron & Low; running date line 11 July 1958 on held scan; pages from project extract of this PDF",
    useful="Y", reason="Named maintenance medium; serum inhibitors",
    fulltext="Y", lead_source="round9_snowball", round="10", paper_spine="Y", alias_of="",
    notes="No DOI printed on held scan. Prior invented DOI/PMID removed.",
),
R(
    id="P1-049", year="1961",
    authors="Hayflick L, Moorhead PS",
    title="The serial cultivation of human diploid cell strains",
    journal_or_source="Exp Cell Res",
    citation="Hayflick L, Moorhead PS. The serial cultivation of human diploid cell strains. Exp Cell Res. 1961 (lead; PDF not held)",
    short_cite="Hayflick & Moorhead 1961",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="B", reason="Diploid strain standard lead",
    fulltext="N", lead_source="round9_snowball", round="9", paper_spine="N", alias_of="",
    notes="No machine ID without held PDF.",
),
R(
    id="P1-050", year="1952",
    authors="Robbins FC, Weller TH, Enders JF",
    title="Studies on the cultivation of poliomyelitis viruses in tissue culture. II. … (roller-tube)",
    journal_or_source="J Immunol",
    citation="Robbins et al. Studies on the cultivation of poliomyelitis viruses in tissue culture. II. J Immunol. 1952 (lead; PDF not held)",
    short_cite="Robbins et al. 1952 J Immunol II",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="",
    useful="B", reason="Enders group methods lead",
    fulltext="N", lead_source="round9_snowball", round="9", paper_spine="N", alias_of="",
    notes="",
),
R(
    id="P1-051", year="1948",
    authors="Weller TH, Enders JF",
    title="Production of hemagglutinin by mumps and influenza A viruses in suspended cell tissue cultures",
    journal_or_source="Proc Soc Exp Biol Med",
    citation="Proc Soc Exp Biol Med. 1948;69:124-128",
    short_cite="Weller & Enders 1948 mumps influenza HA TC",
    doi="", pmid="", pmcid="",
    other_id="16638", other_id_type="psgbm_article_number",
    stable_url="",
    id_basis="PDF: title, authors, pages 124-128, article number 16638",
    useful="Y", reason="Pre-polio ultrafiltrate medium HS",
    fulltext="Y", lead_source="handoff_priority_A", round="10", paper_spine="optional", alias_of="",
    notes="No DOI printed on PDF. Article number 16638 certain.",
),
R(
    id="P1-200", year="1961",
    authors="Smith SE",
    title="A maintenance medium for tissue culture virus studies",
    journal_or_source="Br J Exp Pathol",
    citation="Br J Exp Pathol. 1961;42:232-235",
    short_cite="Smith 1961 maintenance medium",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="PDF: title, author, pages start 232; year from journal imprint in extract",
    useful="Y", reason="Defines maintenance medium for virus studies",
    fulltext="Y", lead_source="user_pdf", round="6", paper_spine="N", alias_of="",
    notes="Prior PMCID removed — not printed on held PDF first pages.",
),
R(
    id="P1-201", year="1961",
    authors="Hsiung GD",
    title="Applications of primary cell cultures in the study of animal viruses",
    journal_or_source="Yale J Biol Med",
    citation="Yale J Biol Med (Hsiung GD; Applications of primary cell cultures in the study of animal viruses)",
    short_cite="Hsiung 1961 primary cell cultures",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="PDF: title, author, Yale Journal of Biology and Medicine running head",
    useful="Y", reason="Primary cell culture virus methods review; serum overlay factors",
    fulltext="Y", lead_source="user_pdf", round="6", paper_spine="N", alias_of="",
    notes="Volume/pages not asserted without clear PDF imprint capture.",
),
R(
    id="P1-203", year="1964",
    authors="Boyle JJ",
    title="Rift Valley Fever Virus Assay in Serum-Free Hamster Kidney Monolayers",
    journal_or_source="U.S. Army Biological Laboratories Technical Manuscript 132",
    citation="Same as P1-018; DTIC AD0437967",
    short_cite="Boyle 1964 (alias P1-018)",
    doi="", pmid="", pmcid="",
    other_id="AD0437967", other_id_type="dtic_ad",
    stable_url="",
    id_basis="Alias of P1-018",
    useful="Y", reason="duplicate_alias_of_P1-018",
    fulltext="Y", lead_source="user_pdf", round="7", paper_spine="N", alias_of="P1-018",
    notes="",
),
R(
    id="P1-204", year="1963",
    authors="Rosenbaum MJ, et al.",
    title="A simplified method for virus-tissue culture procedures in microtitration plates",
    journal_or_source="DTIC",
    citation="Same as P1-035; DTIC AD0411928",
    short_cite="Rosenbaum (alias P1-035)",
    doi="", pmid="", pmcid="",
    other_id="AD0411928", other_id_type="dtic_ad",
    stable_url="",
    id_basis="Alias of P1-035",
    useful="Y", reason="duplicate_alias_of_P1-035",
    fulltext="Y", lead_source="user_pdf", round="7", paper_spine="N", alias_of="P1-035",
    notes="",
),
R(
    id="P1-205", year="1972",
    authors="Schmidt NJ",
    title="Tissue culture in the laboratory diagnosis of viral infections",
    journal_or_source="Am J Clin Pathol",
    citation="Am J Clin Pathol. 1972;57:820-828",
    short_cite="Schmidt 1972 AJCP",
    doi="", pmid="", pmcid="", other_id="", other_id_type="", stable_url="",
    id_basis="PDF abstract line: Am. J. Clin. Pathol. 57: 820-828, 1972",
    useful="Y", reason="Diagnostic TC review",
    fulltext="Y", lead_source="user_pdf", round="9", paper_spine="N", alias_of="",
    notes="No DOI on PDF.",
),
R(
    id="P1-206", year="1953",
    authors="Melnick JL",
    title="Poliomyelitis virus in tissue culture (dry-tube / bottle culture methods)",
    journal_or_source="Proc Soc Exp Biol Med",
    citation="Proc Soc Exp Biol Med. 1953;84:558-563",
    short_cite="Melnick 1953 dry-tube bottle",
    # PDF pages 558+
    doi="", pmid="", pmcid="",
    other_id="", other_id_type="",
    stable_url="",
    id_basis="PDF pages 558+ title running head; year/volume from project extract of held PDF",
    useful="Y", reason="10% bovine+199 growth; wash; no-serum maintenance",
    fulltext="Y", lead_source="user_pdf", round="9", paper_spine="Y", alias_of="",
    notes="Paper spine. No DOI printed on held PDF — left blank.",
),
]


def main() -> None:
    rows = sorted(
        ROWS,
        key=lambda r: (
            r["id"][:2],
            int("".join(c for c in r["id"] if c.isdigit()) or 0),
            r["id"],
        ),
    )
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    n = len(rows)
    with_doi = sum(1 for r in rows if r["doi"])
    with_pmid = sum(1 for r in rows if r["pmid"])
    with_pmc = sum(1 for r in rows if r["pmcid"])
    with_other = sum(1 for r in rows if r["other_id"])
    with_any = sum(
        1 for r in rows if r["doi"] or r["pmid"] or r["pmcid"] or r["other_id"]
    )
    spine = [r["id"] for r in rows if r["paper_spine"] == "Y"]

    readme = f"""# P1 research bibliography (public)

**File of record:** [`P1_screened.csv`](P1_screened.csv)  
**Purpose:** Full list of sources **screened** during P1 historical research (useful, borderline, not useful).  
The published paper can point reviewers here.

**Paper-facing subset:** [`P1_for_paper.md`](P1_for_paper.md)  
**Extracts:** [`P1_useful.csv`](P1_useful.csv), [`P1_quotes.md`](P1_quotes.md)

---

## Integrity rule (read this)

**If an identifier is not certain, the field is left blank.**

We do **not** invent DOI, PMID, PMCID, volume, or pages to look complete.  
A reviewer who needs more can use `citation` + `title` + `authors` + `year` + `notes` / `id_basis`.

| Field | When filled |
|-------|-------------|
| `doi` | Printed on held PDF, or PSGBM DOI matching article number on PDF/filename (documented in `id_basis`) |
| `pmid` | Only if verified on a held source (currently often blank) |
| `pmcid` | Only if in our PMC-sourced PDF filename or printed on PDF |
| `other_id` | DTIC AD on PDF, CLSI code, PSGBM article number on PDF, book key, etc. |
| `stable_url` | Only when it is a durable resolver for a filled ID (e.g. `https://doi.org/...`) or official Nobel URL |

`id_basis` always explains **why** any machine ID is present (or is empty).

---

## Counts (this build)

| Metric | n |
|--------|---|
| Screened rows | {n} |
| Rows with any machine ID | {with_any} |
| With DOI | {with_doi} |
| With PMID | {with_pmid} |
| With PMCID | {with_pmc} |
| With other_id | {with_other} |
| Paper spine (`paper_spine=Y`) | {len(spine)}: {', '.join(spine)} |

---

## Column dictionary

| Column | Meaning |
|--------|---------|
| `id` | Project ID `P1-###` |
| `year` | Year if known; else blank |
| `authors` / `title` / `journal_or_source` / `citation` | Bibliographic text (may be incomplete if unknown) |
| `doi` / `pmid` / `pmcid` | Machine IDs **only if certain** |
| `other_id` / `other_id_type` | Non-DOI/PMID identifier when certain |
| `stable_url` | Resolver URL only when justified |
| `id_basis` | Evidence for any filled machine ID |
| `useful` | `Y` / `B` / `N` screen result |
| `reason` | Screen reason |
| `fulltext` | `Y` / `partial` / `N` |
| `lead_source` / `round` | How/when entered |
| `paper_spine` | `Y` / `optional` / `institutional` / `N` |
| `alias_of` | Canonical ID if duplicate |
| `notes` | Free notes |

---

## Aliases

| Alias | Canonical |
|-------|-----------|
| P1-019 | P1-048 |
| P1-020 | P1-014 |
| P1-028 | P1-010 |
| P1-036 | P1-008 |
| P1-203 | P1-018 |
| P1-204 | P1-035 |

---

## Rebuild

```text
python p1_history/_notes/build_p1_bibliography.py
```

Edit `ROWS` in that script; re-run; commit CSV + this README.

---

*Incomplete identifiers are intentional. Incorrect identifiers are not.*
"""
    README.write_text(readme, encoding="utf-8")
    print(f"Wrote {OUT} n={n} any_id={with_any} doi={with_doi} pmid={with_pmid} pmc={with_pmc}")


if __name__ == "__main__":
    main()
