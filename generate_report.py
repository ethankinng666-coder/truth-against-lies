#!/usr/bin/env python3
"""Generate comprehensive site report PDF for Truth Against Lies."""

from fpdf import FPDF
import os

class SiteReport(FPDF):
    def __init__(self):
        super().__init__()
        # Use Arial Unicode for Hebrew support
        font_path = '/Library/Fonts/Arial Unicode.ttf'
        if os.path.exists(font_path):
            self.add_font('ArialUni', '', font_path, )
            self.add_font('ArialUni', 'B', font_path, )
            self.font_name = 'ArialUni'
        else:
            self.font_name = 'Helvetica'
        self.gold = (226, 183, 20)
        self.dark = (10, 10, 26)
        self.white = (224, 224, 224)
        self.red = (231, 76, 60)
        self.green = (46, 204, 113)
        self.blue = (52, 152, 219)
        self.gray = (150, 150, 150)

    def header(self):
        if self.page_no() > 1:
            self.set_font(self.font_name, '', 8)
            self.set_text_color(*self.gray)
            self.cell(0, 8, f'Truth Against Lies - Site Report | Page {self.page_no()}', align='C')
            self.ln(12)

    def footer(self):
        self.set_y(-15)
        self.set_font(self.font_name, '', 7)
        self.set_text_color(*self.gray)
        self.cell(0, 10, 'Generated March 2026 | truth-against-lies.github.io/truth-against-lies/', align='C')

    def title_page(self):
        self.add_page()
        self.ln(60)
        self.set_font(self.font_name, 'B', 32)
        self.set_text_color(*self.gold)
        self.cell(0, 15, 'Truth Against Lies', align='C')
        self.ln(18)
        self.set_font(self.font_name, '', 14)
        self.set_text_color(*self.white)
        self.cell(0, 10, 'Comprehensive Site Report', align='C')
        self.ln(30)
        self.set_font(self.font_name, '', 11)
        self.set_text_color(*self.gray)
        self.cell(0, 8, 'March 2026', align='C')
        self.ln(8)
        self.cell(0, 8, 'truth-against-lies.github.io/truth-against-lies/', align='C')
        self.ln(30)
        self.set_font(self.font_name, '', 10)
        self.set_text_color(*self.white)
        lines = [
            'This document provides a complete overview of the Truth Against Lies website:',
            'its content, structure, technical features, translation system,',
            'and recommendations for future development.',
            '',
            'Built by Nathanael Assis | Assisted by Claude',
        ]
        for line in lines:
            self.cell(0, 7, line, align='C')
            self.ln(7)

    def section_title(self, num, title):
        self.ln(5)
        self.set_font(self.font_name, 'B', 16)
        self.set_text_color(*self.gold)
        self.cell(0, 12, f'{num}. {title}')
        self.ln(10)
        # Gold line
        self.set_draw_color(*self.gold)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(6)

    def sub_title(self, title):
        self.set_font(self.font_name, 'B', 12)
        self.set_text_color(*self.blue)
        self.cell(0, 9, title)
        self.ln(8)

    def sub_sub_title(self, title):
        self.set_font(self.font_name, 'B', 10)
        self.set_text_color(*self.green)
        self.cell(0, 8, title)
        self.ln(7)

    def body_text(self, text):
        self.set_font(self.font_name, '', 10)
        self.set_text_color(*self.white)
        self.multi_cell(0, 6, text)
        self.ln(3)

    def bullet(self, text):
        self.set_font(self.font_name, '', 10)
        self.set_text_color(*self.white)
        x = self.get_x()
        self.cell(8, 6, chr(8226))
        self.multi_cell(0, 6, text)
        self.ln(1)

    def stat_box(self, label, value):
        self.set_font(self.font_name, 'B', 10)
        self.set_text_color(*self.gold)
        self.cell(30, 6, value)
        self.set_font(self.font_name, '', 10)
        self.set_text_color(*self.white)
        self.cell(0, 6, label)
        self.ln(6)

    def check_page_break(self, h=40):
        if self.get_y() + h > 270:
            self.add_page()


def main():
    pdf = SiteReport()
    pdf.set_auto_page_break(True, margin=20)

    # === TITLE PAGE ===
    pdf.title_page()

    # === TABLE OF CONTENTS ===
    pdf.add_page()
    pdf.set_font(pdf.font_name, 'B', 18)
    pdf.set_text_color(*pdf.gold)
    pdf.cell(0, 12, 'Table of Contents')
    pdf.ln(15)

    toc = [
        '1. General Description - Purpose, Audience, Languages',
        '2. Pages & Sections Overview',
        '3. Complete Content Inventory',
        '    3.1  About Section (What is Antisemitism?)',
        '    3.2  34 Claims & Refutations (8 Categories)',
        '    3.3  Common Lies Section (4 Lies)',
        '    3.4  Timeline (12 Historical Events)',
        '    3.5  Psychology Section (6 Mechanisms)',
        '    3.6  Regions Section (7 Geographic Areas)',
        '    3.7  Gallery Section (Historical Documentation)',
        '    3.8  YouTube Section (15+ Videos)',
        '    3.9  Strengthen the People (5 Tabs, 12 Topics)',
        '    3.10 Report Antisemitism',
        '    3.11 Action Page (What Can You Do?)',
        '4. Technical Features',
        '    4.1  Translation System (12 Languages + Google Translate)',
        '    4.2  Search Engine',
        '    4.3  Navigation & Mobile',
        '    4.4  Sharing & Donation',
        '5. What Works Well',
        '6. What Is Missing / Needs Improvement',
        '7. Recommendations for Next Steps',
    ]
    pdf.set_font(pdf.font_name, '', 10)
    pdf.set_text_color(*pdf.white)
    for item in toc:
        pdf.cell(0, 7, item)
        pdf.ln(7)

    # =======================================================
    # SECTION 1: GENERAL DESCRIPTION
    # =======================================================
    pdf.add_page()
    pdf.section_title('1', 'General Description')

    pdf.sub_title('Purpose')
    pdf.body_text(
        'Truth Against Lies is an educational website dedicated to combating antisemitism through '
        'facts, academic research, and historical documentation. It addresses 34 common antisemitic '
        'claims with factual refutations, psychological explanations, and historical context.'
    )
    pdf.body_text(
        'In March 2026, a major new section was added: "Strengthen the People" - shifting the focus '
        'from only countering hatred to also empowering the Jewish people with knowledge, pride, and unity.'
    )

    pdf.sub_title('Target Audience')
    pdf.bullet('Jews who want to learn their history and respond to antisemitism')
    pdf.bullet('Educators and students researching antisemitism')
    pdf.bullet('Social media activists who encounter antisemitic claims')
    pdf.bullet('Anyone interested in understanding antisemitism and fighting it')

    pdf.sub_title('Language Support')
    pdf.body_text('Primary language: Hebrew (RTL)')
    pdf.body_text('12 custom JSON translations: English, Arabic, French, German, Spanish, Portuguese, Russian, Polish, Norwegian, Swedish, Italian, Turkish')
    pdf.body_text('63+ additional languages via Google Translate fallback')
    pdf.body_text('Total: 75+ languages accessible')

    pdf.sub_title('Technical Stack')
    pdf.bullet('Static HTML/CSS/JS hosted on GitHub Pages')
    pdf.bullet('No build system, no framework - pure HTML')
    pdf.bullet('Repository: github.com/truth-against-lies/truth-against-lies')
    pdf.bullet('Domain: truth-against-lies.github.io/truth-against-lies/')

    pdf.sub_title('Design')
    pdf.bullet('Dark theme: #0a0a1a background')
    pdf.bullet('Gold accent: #e2b714')
    pdf.bullet('Professional, serious tone')
    pdf.bullet('Responsive (mobile-first)')

    # =======================================================
    # SECTION 2: PAGES & SECTIONS
    # =======================================================
    pdf.add_page()
    pdf.section_title('2', 'Pages & Sections Overview')

    pdf.sub_title('File Inventory')
    files = [
        ('index.html', '283 KB, ~4,170 lines', 'Main site with all content'),
        ('action.html', '20 KB, 429 lines', '"What can you do?" page'),
        ('gallery.html', '27 KB, 493 lines', 'Historical photo gallery with content warning'),
        ('lang/en.json', '127 KB', 'English translation'),
        ('lang/ar.json', '70 KB', 'Arabic translation'),
        ('lang/fr.json', '147 KB', 'French translation'),
        ('lang/de.json', '140 KB', 'German translation'),
        ('lang/es.json', '138 KB', 'Spanish translation'),
        ('lang/pt.json', '136 KB', 'Portuguese translation'),
        ('lang/ru.json', '210 KB', 'Russian translation (largest - Cyrillic)'),
        ('lang/pl.json', '136 KB', 'Polish translation'),
        ('lang/no.json', '127 KB', 'Norwegian translation'),
        ('lang/sv.json', '129 KB', 'Swedish translation'),
        ('lang/it.json', '137 KB', 'Italian translation'),
        ('lang/tr.json', '137 KB', 'Turkish translation'),
        ('translate.py', '5.9 KB', 'Full translation automation script'),
        ('translate_strengthen.py', '4.7 KB', 'Targeted strengthen section translator'),
    ]
    for name, size, desc in files:
        pdf.set_font(pdf.font_name, 'B', 9)
        pdf.set_text_color(*pdf.gold)
        pdf.cell(50, 6, name)
        pdf.set_font(pdf.font_name, '', 9)
        pdf.set_text_color(*pdf.gray)
        pdf.cell(35, 6, size)
        pdf.set_text_color(*pdf.white)
        pdf.cell(0, 6, desc)
        pdf.ln(6)

    pdf.ln(5)
    pdf.sub_title('Sections in index.html (11 sections)')
    sections = [
        ('#about', 'What is Antisemitism? - 3 intro cards'),
        ('#claims', '34 Claims & Refutations in 8 categories'),
        ('#lies', '4 Modern Lies with share buttons'),
        ('#timeline', '12 Historical Events (2,500 years)'),
        ('#psychology', '6 Psychological Mechanisms'),
        ('#regions', '7 Geographic Regions'),
        ('#gallery', 'Historical Documentation (links to gallery.html)'),
        ('#report', 'Report Antisemitism (links to organizations)'),
        ('#youtube', '15+ Educational Videos in 4 topic groups'),
        ('#strengthen', 'Strengthen the People - 5 tabs, 12 topics (NEW)'),
        ('Footer', 'Donation, credits, sources'),
    ]
    for sid, desc in sections:
        pdf.set_font(pdf.font_name, 'B', 10)
        pdf.set_text_color(*pdf.gold)
        pdf.cell(30, 7, sid)
        pdf.set_font(pdf.font_name, '', 10)
        pdf.set_text_color(*pdf.white)
        pdf.cell(0, 7, desc)
        pdf.ln(7)

    # =======================================================
    # SECTION 3: COMPLETE CONTENT INVENTORY
    # =======================================================
    pdf.add_page()
    pdf.section_title('3', 'Complete Content Inventory')

    # 3.1 About
    pdf.sub_title('3.1 About Section - "What is Antisemitism?"')
    pdf.body_text('3 introduction cards explaining:')
    pdf.bullet('A Hatred That Shapeshifts - antisemitism morphs across eras (religious, racial, political, economic)')
    pdf.bullet('Why Documentation Matters - 34 claims, 8 categories, factual + psychological + historical layers')
    pdf.bullet('Three Layers of Response - Green (facts), Blue (psychology), Gold (history)')

    # 3.2 Claims
    pdf.check_page_break(60)
    pdf.sub_title('3.2 The 34 Claims & 8 Categories')
    pdf.body_text('Each claim includes: title, factual refutation, psychological explanation, and academic sources.')
    pdf.ln(3)

    categories = [
        ('Category 1: Religious & Theological', 7, [
            'Jews killed Jesus', 'Jews are Satan\'s children', 'Blood libel (ritual murder)',
            'Desecration of communion', 'Jews poison wells/spread plague',
            'Jews cursed to wander without homeland', 'Talmud contains hatred'
        ]),
        ('Category 2: Racial & Biological', 3, [
            'Jews are inferior race', 'Genetic predisposition to greed', 'Jews are subhuman'
        ]),
        ('Category 3: Economic & Financial', 5, [
            'Jews control banks/finance', 'Jews are greedy',
            'Jews caused 2008 financial crisis', 'Jews exploit non-Jews',
            '(+ Rothschild conspiracy)'
        ]),
        ('Category 4: Political Conspiracies', 4, [
            'Jews secretly control governments (ZOG)', 'Jews control media',
            'Dual loyalty', '9/11 conspiracy'
        ]),
        ('Category 5: Cultural & Social', 4, [
            'Jews created Communism', 'Jews are tribal/clannish',
            'Jews think they\'re superior ("chosen people")', 'Jews control Hollywood'
        ]),
        ('Category 6: Modern Anti-Zionist', 5, [
            'Physical identification of Jews', 'Israel = Nazi state',
            'Israel has no right to exist', 'AIPAC controls US policy',
            '(+ anti-Zionism as antisemitism)'
        ]),
        ('Category 7: Holocaust Denial', 2, [
            'Holocaust didn\'t happen', 'Jews exaggerated the Holocaust'
        ]),
        ('Category 8: Online & Contemporary', 4, [
            '((Echoes)) and coded symbols', 'Jews created COVID',
            'Great Replacement conspiracy', 'Jews weaponize antisemitism claims'
        ]),
    ]

    for cat_name, count, claims in categories:
        pdf.check_page_break(30)
        pdf.sub_sub_title(f'{cat_name} ({count} claims)')
        for c in claims:
            pdf.bullet(c)
        pdf.ln(2)

    # 3.3 Lies
    pdf.check_page_break(50)
    pdf.sub_title('3.3 Common Lies Section (4 Modern Lies)')
    pdf.body_text('Each lie card includes: the claim, factual refutation with bullet points, sources, and share buttons (WhatsApp, Twitter/X, Telegram, Facebook, Copy).')
    lies = [
        'Israel committed genocide in Gaza',
        'Israel pushed Trump to fight Iran',
        'Israel is an apartheid state',
        'Jews control media and world finance',
    ]
    for lie in lies:
        pdf.bullet(f'"{lie}"')

    # 3.4 Timeline
    pdf.check_page_break(80)
    pdf.sub_title('3.4 Timeline (12 Historical Events)')
    timeline = [
        ('167 BCE', 'Antiochus IV persecution', 'First state-organized persecution'),
        ('38 CE', 'Alexandria pogrom', 'First documented anti-Jewish riot'),
        ('70 CE', 'Temple destruction', 'Beginning of diaspora'),
        ('1096', 'First Crusade massacres', '5,000-10,000 murdered'),
        ('1144', 'First blood libel (Norwich)', 'Template for centuries of accusations'),
        ('1215', 'Fourth Lateran Council', 'Badges, restrictions, ghettos'),
        ('1290', 'Expulsion from England', '3,000-16,000 expelled'),
        ('1348-1351', 'Black Death pogroms', '200+ communities destroyed'),
        ('1478', 'Spanish Inquisition', '3,000-5,000 executed'),
        ('1492', 'Expulsion from Spain', '200,000 expelled'),
        ('1933-1945', 'The Holocaust', '6,000,000 murdered'),
        ('2018-2024', 'Global antisemitism wave', '167% increase (ADL data)'),
    ]
    for date, event, detail in timeline:
        pdf.set_font(pdf.font_name, 'B', 9)
        pdf.set_text_color(*pdf.gold)
        pdf.cell(25, 6, date)
        pdf.set_font(pdf.font_name, 'B', 9)
        pdf.set_text_color(*pdf.white)
        pdf.cell(55, 6, event)
        pdf.set_font(pdf.font_name, '', 9)
        pdf.set_text_color(*pdf.gray)
        pdf.cell(0, 6, detail)
        pdf.ln(6)

    # 3.5 Psychology
    pdf.check_page_break(50)
    pdf.sub_title('3.5 Psychology Section (6 Mechanisms)')
    mechanisms = [
        ('Scapegoating', 'Blaming a minority group for society\'s problems'),
        ('Projection', 'Attributing one\'s own negative traits to others'),
        ('Confirmation Bias', 'Seeking evidence that confirms pre-existing beliefs'),
        ('Illusory Correlation', 'Overestimating the connection between minority and negative events'),
        ('Authoritarian Personality', 'Adorno\'s framework: rigid thinking, obedience, out-group hostility'),
        ('Conspiracy Thinking', 'Pattern-seeking in unrelated events, need for simple explanations'),
    ]
    for name, desc in mechanisms:
        pdf.set_font(pdf.font_name, 'B', 10)
        pdf.set_text_color(*pdf.green)
        pdf.cell(45, 7, name)
        pdf.set_font(pdf.font_name, '', 10)
        pdf.set_text_color(*pdf.white)
        pdf.cell(0, 7, desc)
        pdf.ln(7)

    pdf.ln(3)
    pdf.body_text('Key Insight: Antisemitism exists even in countries with almost no Jews (Japan, South Korea) - proving it\'s about the antisemite\'s psychology, not about real Jews.')

    # 3.6 Regions
    pdf.check_page_break(60)
    pdf.sub_title('3.6 Regions Section (7 Geographic Areas)')
    regions = [
        ('Islamic/Arab World', 'Historical context, Hamas Charter, 850,000 Jewish refugees expelled'),
        ('Poland & Eastern Europe', 'Pogroms, "Zydokomuna" myth, Jedwabne massacre (1941)'),
        ('Nazi Germany', 'Escalation 1933-1945, industrial genocide, 6 million murdered'),
        ('Modern Western Europe', '"Anti-Zionism" as new antisemitism, France (Halimi), UK (Corbyn)'),
        ('United States', 'Far-right (Pittsburgh, Charlottesville), Farrakhan, campus BDS'),
        ('Iran & Islamic Theocracy', 'State-level Holocaust denial, terror funding (Hezbollah, Hamas)'),
        ('Japan, South Korea & East Asia', '"Antisemitism without Jews" - proves hatred is fantasy-based'),
    ]
    for name, desc in regions:
        pdf.check_page_break(15)
        pdf.set_font(pdf.font_name, 'B', 10)
        pdf.set_text_color(*pdf.gold)
        pdf.cell(55, 7, name)
        pdf.set_font(pdf.font_name, '', 9)
        pdf.set_text_color(*pdf.white)
        pdf.multi_cell(0, 7, desc)
        pdf.ln(1)

    # 3.7 Gallery
    pdf.check_page_break(30)
    pdf.sub_title('3.7 Gallery Section')
    pdf.body_text('Separate page (gallery.html) with content warning gate before entry.')
    pdf.body_text('Categories: Holocaust (1933-1945), October 7 (2023), Terror attacks, Antisemitism worldwide, Israeli wars.')
    pdf.body_text('Features: Tab-based category filters, lightbox viewer with navigation, captions with source attribution, lazy loading.')
    pdf.body_text('Sources: Wikimedia Commons, Yad Vashem, USHMM, IDF archives.')

    # 3.8 YouTube
    pdf.check_page_break(50)
    pdf.sub_title('3.8 YouTube Section (15+ Videos)')
    pdf.body_text('Educational videos organized by 4 topic groups:')
    pdf.sub_sub_title('Topic 1: Roots of Hatred (5 videos)')
    pdf.bullet('Unpacked: Why does antisemitism still exist?')
    pdf.bullet('Unpacked: Who\'s responsible for antisemitism?')
    pdf.bullet('Unpacked: Is the Talmud Satanic?')
    pdf.bullet('Henry Abramson: Medieval antisemitism')
    pdf.bullet('Henry Abramson: Fourth Lateran Council (1215)')

    pdf.sub_sub_title('Topic 2: Myths & Conspiracies (4 videos)')
    pdf.bullet('Unpacked: Do Rothschilds control the world?')
    pdf.bullet('Unpacked: Sources of conspiracy theories')
    pdf.bullet('Unpacked: When antisemitism becomes political')
    pdf.bullet('Unpacked: Can Jews be antisemitic?')

    pdf.sub_sub_title('Topic 3: Holocaust & Memory (2 videos)')
    pdf.bullet('Unpacked: Kristallnacht')
    pdf.bullet('CrashCourse: Holocaust, genocide, WWII')

    pdf.sub_sub_title('Topic 4: Israel & History (3 videos)')
    pdf.bullet('Unpacked: Are Jews native to Israel?')
    pdf.bullet('Unpacked: Spanish Inquisition')
    pdf.bullet('Unpacked: Dreyfus Affair')

    pdf.check_page_break(20)
    pdf.sub_sub_title('Recommended Channels (6)')
    pdf.bullet('Unpacked, Henry Abramson, CrashCourse, CAMERA, The Watchman, Brother Rachid')

    # 3.9 Strengthen
    pdf.add_page()
    pdf.sub_title('3.9 Strengthen the People - NEW SECTION (5 Tabs, 12 Topics)')
    pdf.body_text('Added March 2026. Content based on 11 research PDFs ("The Inner Faces of Israel"). This section shifts focus from countering antisemites to empowering the Jewish people.')

    str_tabs = [
        ('Tab 0: Who We Are', [
            ('The Jewish Mosaic - One People, A Thousand Faces',
             'Beta Israel (Ethiopia, 170,000), Bene Israel (India, 2,100 years), Kaifeng (China, 1,000 years), Kurdish Jews (Aramaic, 2,700 years), Bukharan Jews (Silk Road, 2,500 years), Mountain Jews (Caucasus warriors), Yemenite Jews (Magic Carpet, 49,000), Anusim/Crypto-Jews (500 years secret)'),
            ('Israel From Within - 9.8 Million From 100 Countries',
             'Demographics (73.5% Jewish, 21% Arab, 5.5% other). Druze (blood covenant, 430+ fallen), Bedouin (desert trackers), Christian Arabs (only growing community in Middle East), Circassians (5,000 warriors), Mizrahi/Sephardi (850,000 refugees), Russian Aliyah (1 million, 60% degrees)'),
        ]),
        ('Tab 1: Where We Came From', [
            ('Zionism - From Dream to State',
             'Pre-Herzl roots, Herzl & Der Judenstaat (1896), Basel Congress (1897), Five Aliyot (1882-1939), Balfour Declaration (67 words), British Mandate betrayal, Underground movements, UN Vote Nov 29 1947, Declaration of Independence May 14 1948 (32 min, 25 signatures)'),
            ('3,500 Years of Survival',
             'Every persecutor vanished (Egypt, Assyria, Babylon, Greece, Rome, Crusaders, Inquisition, Nazis). We survived through education, family, community, the book, and memory.'),
        ]),
        ('Tab 2: What We Gave the World', [
            ('0.2% of Population, 25% of Nobel Prizes',
             'Medicine (Salk, Ehrlich, Waksman), Physics (Einstein, Feynman, Bohr), Tech (Google, Facebook, Oracle, Waze, Iron Dome), Arts (Spielberg, Dylan, Streisand), Law/Philosophy (Freud, Chomsky, Kahneman, RBG)'),
            ('Righteous Among the Nations - Light in the Darkness',
             '28,217 people from 51 countries. Schindler (1,200), Wallenberg (100,000), Sugihara (2,139 visas in 29 days), Sendler (2,500 children), Winton (669 children, 50 years silence). Collective: Le Chambon (3,500), Denmark (99%), Albania, Bulgaria (48,000)'),
        ]),
        ('Tab 3: Our Unity', [
            ('Unity in Times of Trial',
             'Wars that united (1948, 1967, 1973). Altalena affair. October 7 - moment of unity.'),
            ('Secular and Religious - The Internal Tension',
             'Spectrum: 45% secular, 25% traditional, 13% ultra-Orthodox, 12% religious-Zionist. 2023 protests. Oct 7 healed rifts temporarily.'),
            ('Internal Betrayal - Jews Against Israel',
             'Figures: Ilan Pappe, Finkelstein, Gideon Levy, Shlomo Sand. Orgs: JVP, IfNotNow, B\'Tselem, Breaking the Silence. Why it\'s dangerous: provides legitimacy to antisemites.'),
        ]),
        ('Tab 4: Where From Here', [
            ('October 7 - The Day Everything Changed',
             '1,139-1,219 murdered, 251 kidnapped. Nova festival (364), Kfar Aza, Be\'eri, Nir Oz. Hero stories. Intelligence failure.'),
            ('The Palestinian Narrative vs. Reality',
             '5.9M "refugees" (unique UNRWA status). "Right of return" = end of Israel. 850,000 Jewish refugees nobody mentions. "Apartheid" debunked (2M Arab citizens, Arab Supreme Court judge convicted Jewish president).'),
            ('Antisemitism After October 7 - The Numbers',
             '360% rise US, 589% UK, 738% Canada, 1,000% France. 100+ university campuses. Amsterdam pogrom Nov 2024. What to do: education, intellectual response, unity, pride.'),
        ]),
    ]

    for tab_name, topics in str_tabs:
        pdf.check_page_break(40)
        pdf.sub_sub_title(tab_name)
        for topic_title, topic_desc in topics:
            pdf.check_page_break(25)
            pdf.set_x(10)
            pdf.set_font(pdf.font_name, 'B', 9)
            pdf.set_text_color(*pdf.white)
            pdf.multi_cell(190, 6, topic_title)
            pdf.set_x(10)
            pdf.set_font(pdf.font_name, '', 8)
            pdf.set_text_color(*pdf.gray)
            pdf.multi_cell(190, 5, topic_desc)
            pdf.ln(3)

    # 3.10 Report
    pdf.check_page_break(30)
    pdf.sub_title('3.10 Report Antisemitism')
    pdf.body_text('Links to major reporting organizations and platforms for reporting antisemitic incidents online and offline.')

    # 3.11 Action Page
    pdf.check_page_break(50)
    pdf.sub_title('3.11 Action Page (action.html)')
    pdf.body_text('Separate page with 3 sections:')
    pdf.bullet('How to Report Antisemitism - 5-step process, platform-specific links (ADL, Facebook, Instagram, TikTok, X, YouTube)')
    pdf.bullet('How to Share the Site - Social media buttons (WhatsApp, Facebook, X, Telegram, Copy Link)')
    pdf.bullet('Organizations Fighting Antisemitism - 12 organizations: ADL (1913), Simon Wiesenthal Center (1977), Yad Vashem (1953), USHMM (1993), IHRA (1998), AJC (1906), StandWithUs (2001), UN Watch (1993), CAMERA (1982), Canary Mission, CAM (2019), WJC (1936)')

    # =======================================================
    # SECTION 4: TECHNICAL FEATURES
    # =======================================================
    pdf.add_page()
    pdf.section_title('4', 'Technical Features')

    pdf.sub_title('4.1 Translation System')
    pdf.body_text('Two-tier architecture:')
    pdf.bullet('Tier 1: 12 custom JSON translations loaded from lang/*.json - high quality, full control, works offline')
    pdf.bullet('Tier 2: 63+ languages via Google Translate API - automatic fallback for non-JSON languages')
    pdf.ln(3)
    pdf.body_text('Translation keys structure (34 top-level keys per file):')
    pdf.bullet('meta, nav, ui, hero_*, stat_labels, about_*, claims_*, categories (8x with claims)')
    pdf.bullet('lies_*, timeline (12 items), psych_*, regions (7 cards)')
    pdf.bullet('youtube_title, gallery_title, report_*, strengthen (5 tabs), footer')
    pdf.ln(3)
    pdf.body_text('JavaScript functions: goTranslate(), goOriginal(), loadCustomTranslation(), applyTranslation()')
    pdf.body_text('Language saved in localStorage for persistence across sessions.')

    pdf.sub_title('4.2 Search Engine')
    pdf.body_text('Built-in site search (input box in navbar):')
    pdf.bullet('Searches through: h2, h3, h4, p, claim headers, lie cards, timeline items, region cards, intro cards, stat labels, list items, str-highlight elements')
    pdf.bullet('Highlights matching element and scrolls to it')
    pdf.bullet('Auto-opens collapsed claim cards if match is inside')
    pdf.bullet('Cycles through matches on repeated Enter')

    pdf.sub_title('4.3 Navigation & Mobile')
    pdf.bullet('Fixed navbar with hamburger menu (dropdown on click)')
    pdf.bullet('11 nav links + search box + language selector + donate button')
    pdf.bullet('Smooth scroll to all sections')
    pdf.bullet('Back-to-top button (appears after scrolling 500px)')
    pdf.bullet('Mobile responsive: media queries for <768px and <600px')
    pdf.bullet('Fade-in animation on scroll (IntersectionObserver)')

    pdf.sub_title('4.4 Sharing & Donation')
    pdf.bullet('Lie cards: Copy response + Share to WhatsApp/X/Telegram/Facebook')
    pdf.bullet('Donation: Buy Me A Coffee link in navbar + footer')
    pdf.bullet('URL: buymeacoffee.com/nathaniellinder')

    # =======================================================
    # SECTION 5: WHAT WORKS WELL
    # =======================================================
    pdf.add_page()
    pdf.section_title('5', 'What Works Well')

    strengths = [
        ('Massive Content Depth', '34 antisemitic claims fully refuted with 3 layers each (facts + psychology + history). This is rare - most sites only provide factual refutation.'),
        ('Academic Rigor', 'Every claim cites peer-reviewed sources. Hamilton & Gifford (1976), Adorno (1950), ADL data, Yad Vashem, USHMM. This gives credibility.'),
        ('Multi-Language Reach', '12 high-quality custom translations + 63 via Google Translate = 75+ languages. Very few antisemitism resources offer this.'),
        ('Share/Copy System', 'The "copy response" button on lie cards lets users instantly share refutations on social media. This is practical activism.'),
        ('The New "Strengthen" Section', 'Shifts from defensive (countering lies) to empowering (knowing our history). Content based on 11 research PDFs covering diverse Jewish communities, Zionism, contributions, unity, and current challenges.'),
        ('Design Quality', 'Dark/gold theme is professional and serious. Good contrast, readable, consistent across all sections.'),
        ('Single-File Simplicity', 'No build system, no dependencies, no framework. Easy to deploy, maintain, and update. GitHub Pages hosting is free and reliable.'),
        ('Search', 'Works across all sections including the new strengthen section.'),
        ('Psychological Explanations', 'Explaining WHY people believe lies is more powerful than just saying they\'re wrong.'),
    ]
    for title, desc in strengths:
        pdf.check_page_break(20)
        pdf.set_font(pdf.font_name, 'B', 10)
        pdf.set_text_color(*pdf.green)
        pdf.cell(0, 7, f'+ {title}')
        pdf.ln(7)
        pdf.set_font(pdf.font_name, '', 9)
        pdf.set_text_color(*pdf.white)
        pdf.multi_cell(0, 6, desc)
        pdf.ln(3)

    # =======================================================
    # SECTION 6: WHAT IS MISSING / NEEDS IMPROVEMENT
    # =======================================================
    pdf.add_page()
    pdf.section_title('6', 'What Is Missing / Needs Improvement')

    issues = [
        ('No Custom Domain', 'Still using github.io URL. A custom domain (e.g., truth-against-lies.org) would look more professional and be easier to share.'),
        ('Arabic Translation Incomplete', 'ar.json appears to have fewer keys than other language files (70KB vs 127-210KB). May need a full re-translation pass.'),
        ('No Analytics', 'No way to know how many people visit, which sections they read, where they come from. Google Analytics or a privacy-friendly alternative (Plausible, Umami) would help.'),
        ('No SEO Optimization', 'Missing: Open Graph tags for social sharing previews, structured data (JSON-LD), sitemap.xml, robots.txt. Social media shares currently show no preview image or description.'),
        ('Gallery Has No Images Embedded', 'The gallery section in index.html links to gallery.html, but actual images depend on external URLs. If those URLs change, images break.'),
        ('No Offline Support', 'No Service Worker or PWA manifest. Adding this would let the site work offline - important for areas with poor connectivity.'),
        ('Single HTML File Is Getting Large', 'index.html is 283KB and 4,170 lines. This can slow initial page load. Consider lazy-loading sections or splitting into components.'),
        ('October 7 Content Overlap', 'The October 7 massacre is mentioned in: Claims section, Lies section, Regions section, Strengthen section (Tab 4), and Timeline. Some consolidation or cross-linking would reduce repetition.'),
        ('No Newsletter/Email Subscription', 'No way to reach visitors again after they leave. An email list would enable updates and community building.'),
        ('Translation Quality', 'Google Translate output (used for the 12 JSON files) can be awkward. Professional proofreading for key languages (English, French, Arabic, Russian) would improve credibility.'),
        ('Accessibility', 'No ARIA labels on interactive elements, no skip-to-content link, no keyboard navigation for tabs. Screen reader users may struggle.'),
    ]
    for title, desc in issues:
        pdf.check_page_break(20)
        pdf.set_font(pdf.font_name, 'B', 10)
        pdf.set_text_color(*pdf.red)
        pdf.cell(0, 7, f'- {title}')
        pdf.ln(7)
        pdf.set_font(pdf.font_name, '', 9)
        pdf.set_text_color(*pdf.white)
        pdf.multi_cell(0, 6, desc)
        pdf.ln(3)

    # =======================================================
    # SECTION 7: RECOMMENDATIONS
    # =======================================================
    pdf.add_page()
    pdf.section_title('7', 'Recommendations for Next Steps')

    pdf.sub_title('HIGH PRIORITY (Do Soon)')
    recs_high = [
        ('Add Open Graph Meta Tags', 'Add og:title, og:description, og:image to index.html so social media shares show a proper preview. This takes 10 minutes and dramatically improves shareability.'),
        ('Fix Arabic Translation', 'Run a full translation pass on ar.json to match other language files. Arabic is critical given the Middle East context.'),
        ('Add sitemap.xml and robots.txt', 'Basic SEO files that help search engines index the site. Takes 5 minutes.'),
        ('Proofread English Translation', 'The English version is the most important for international reach. Have a native speaker review en.json for awkward phrasing.'),
    ]
    for title, desc in recs_high:
        pdf.check_page_break(15)
        pdf.set_font(pdf.font_name, 'B', 10)
        pdf.set_text_color(*pdf.gold)
        pdf.cell(0, 7, f'1. {title}')
        pdf.ln(7)
        pdf.set_font(pdf.font_name, '', 9)
        pdf.set_text_color(*pdf.white)
        pdf.multi_cell(0, 6, desc)
        pdf.ln(2)

    pdf.sub_title('MEDIUM PRIORITY (This Month)')
    recs_med = [
        ('Add Analytics', 'Plausible.io (privacy-friendly) or Google Analytics. Know your audience.'),
        ('Custom Domain', 'Register truth-against-lies.org and point it to GitHub Pages.'),
        ('Social Sharing Preview Image', 'Create a 1200x630px image for og:image with the site logo and tagline.'),
        ('Add Service Worker', 'Make the site work offline. Especially important for users in areas with unreliable internet.'),
        ('Consolidate October 7 Content', 'Create a dedicated October 7 page or section, and link to it from other sections instead of repeating the content.'),
    ]
    for title, desc in recs_med:
        pdf.check_page_break(15)
        pdf.set_font(pdf.font_name, 'B', 10)
        pdf.set_text_color(*pdf.blue)
        pdf.cell(0, 7, f'2. {title}')
        pdf.ln(7)
        pdf.set_font(pdf.font_name, '', 9)
        pdf.set_text_color(*pdf.white)
        pdf.multi_cell(0, 6, desc)
        pdf.ln(2)

    pdf.sub_title('FUTURE IDEAS')
    recs_future = [
        ('Interactive Quiz', '"Can you spot the antisemitic claim?" - engaging way to teach people to recognize propaganda.'),
        ('Community Contributions', 'Let users submit new claims/refutations for review. Builds community ownership.'),
        ('Video Content', 'Short TikTok/Reels-style videos for each claim. 60-second refutations.'),
        ('WhatsApp Bot', 'Send an antisemitic claim to the bot, get an instant refutation. Uses the existing JSON content.'),
        ('Mobile App (PWA)', 'Turn the site into a Progressive Web App. Install on phone, works offline.'),
        ('Educator Resources', 'Downloadable lesson plans, PowerPoint decks, classroom activities based on site content.'),
        ('Newsletter', 'Monthly email with new antisemitic trends and how to respond. Builds a community.'),
    ]
    for title, desc in recs_future:
        pdf.check_page_break(15)
        pdf.set_font(pdf.font_name, 'B', 10)
        pdf.set_text_color(*pdf.gray)
        pdf.cell(0, 7, f'3. {title}')
        pdf.ln(7)
        pdf.set_font(pdf.font_name, '', 9)
        pdf.set_text_color(*pdf.white)
        pdf.multi_cell(0, 6, desc)
        pdf.ln(2)

    # === FINAL STATS PAGE ===
    pdf.add_page()
    pdf.section_title('', 'Summary Statistics')
    pdf.ln(5)

    stats = [
        ('Total antisemitic claims addressed', '34'),
        ('Categories of antisemitism', '8'),
        ('Historical timeline events', '12'),
        ('Psychological mechanisms explained', '6'),
        ('Geographic regions analyzed', '7'),
        ('Modern lies refuted (with sharing)', '4'),
        ('Strengthen the People tabs', '5'),
        ('Strengthen topics', '12'),
        ('YouTube videos embedded', '15+'),
        ('Recommended YouTube channels', '6'),
        ('Organizations listed', '12'),
        ('Custom language translations', '12'),
        ('Total languages supported', '75+'),
        ('HTML pages', '3'),
        ('Total content size', '~1.8 MB'),
        ('Git commits', '6+'),
    ]
    for label, value in stats:
        pdf.stat_box(label, value)

    pdf.ln(10)
    pdf.set_font(pdf.font_name, 'B', 14)
    pdf.set_text_color(*pdf.gold)
    pdf.cell(0, 12, 'The truth is the most powerful weapon against hatred.', align='C')

    # Save
    output_path = '/Users/nethanellinder/code/truth-against-lies/site_report.pdf'
    pdf.output(output_path)
    print(f'Report saved to {output_path}')
    print(f'Pages: {pdf.page_no()}')

if __name__ == '__main__':
    main()
