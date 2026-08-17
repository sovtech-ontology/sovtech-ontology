named_individuals: dict[str, dict[str, dict[str, str]]] = {
    "AgreementType": {
        "TrustIndenture": {
            "description": (
                "An independent trustee acts on behalf of bondholders and "
                "protects their interests."
            ),
        },
        "FiscalAgencyAgreement": {
            "description": (
                "A fiscal agent appointed by the issuer provides "
                "administrative services; no bondholder representation."
            ),
        },
        "TrustDeed": {
            "description": "English-law analogue of the trust indenture.",
        },
        "LoanAgreement": {
            "description": "A loan, credit, facility, or financing agreement.",
        },
        "Guarantee": {
            "description": "A third party guarantees the obligations.",
        },
        "UnderwritingAgreement": {
            "description": (
                "Underwriting or subscription arrangements for a distribution."
            ),
        },
        "Other": {
            "description": "An agreement not covered by the other categories.",
        },
    },
    "CollectiveActionClauseType": {
        "No": {
            "name": "No CACs",
            "description": "Unanimity required for payment-term changes.",
        },
        "FirstGeneration": {
            "name": "1st Generation CACs",
            "description": "Series-by-series majority modification only.",
        },
        "SecondGeneration": {
            "name": "2nd Generation CACs",
            "description": (
                "Aggregated voting across series with a per-series "
                "requirement (two-limb)."
            ),
        },
        "ThirdGeneration": {
            "name": "3rd Generation Enhanced CACs",
            "description": (
                "Post-2014 ICMA model: adds single-limb aggregated voting "
                "with uniformly applicable treatment."
            ),
        },
    },
    "Country": {
        "ABW": {
            "name": "Aruba",
            "description": "Aruba. ISO 3166-1 ABW / AW / 533. Sovereignty: Netherlands.",
        },
        "AFG": {
            "name": "Afghanistan",
            "description": "Afghanistan. ISO 3166-1 AFG / AF / 004. UN member state.",
        },
        "AGO": {
            "name": "Angola",
            "description": "Angola. ISO 3166-1 AGO / AO / 024. UN member state.",
        },
        "AIA": {
            "name": "Anguilla",
            "description": "Anguilla. ISO 3166-1 AIA / AI / 660. Sovereignty: United Kingdom.",
        },
        "ALA": {
            "name": "Åland Islands",
            "description": "Åland Islands. ISO 3166-1 ALA / AX / 248. Sovereignty: Finland.",
        },
        "ALB": {
            "name": "Albania",
            "description": "Albania. ISO 3166-1 ALB / AL / 008. UN member state.",
        },
        "AND": {
            "name": "Andorra",
            "description": "Andorra. ISO 3166-1 AND / AD / 020. UN member state.",
        },
        "ARE": {
            "name": "United Arab Emirates",
            "description": "United Arab Emirates (the). ISO 3166-1 ARE / AE / 784. UN member state.",
        },
        "ARG": {
            "name": "Argentina",
            "description": "Argentina. ISO 3166-1 ARG / AR / 032. UN member state.",
        },
        "ARM": {
            "name": "Armenia",
            "description": "Armenia. ISO 3166-1 ARM / AM / 051. UN member state.",
        },
        "ASM": {
            "name": "American Samoa",
            "description": "American Samoa. ISO 3166-1 ASM / AS / 016. Sovereignty: United States.",
        },
        "ATA": {
            "name": "Antarctica",
            "description": "Antarctica. ISO 3166-1 ATA / AQ / 010. Sovereignty: Antarctic Treaty.",
        },
        "ATF": {
            "name": "French Southern Territories",
            "description": "French Southern Territories (the). ISO 3166-1 ATF / TF / 260. Sovereignty: France.",
        },
        "ATG": {
            "name": "Antigua and Barbuda",
            "description": "Antigua and Barbuda. ISO 3166-1 ATG / AG / 028. UN member state.",
        },
        "AUS": {
            "name": "Australia",
            "description": "Australia. ISO 3166-1 AUS / AU / 036. UN member state.",
        },
        "AUT": {
            "name": "Austria",
            "description": "Austria. ISO 3166-1 AUT / AT / 040. UN member state.",
        },
        "AZE": {
            "name": "Azerbaijan",
            "description": "Azerbaijan. ISO 3166-1 AZE / AZ / 031. UN member state.",
        },
        "BDI": {
            "name": "Burundi",
            "description": "Burundi. ISO 3166-1 BDI / BI / 108. UN member state.",
        },
        "BEL": {
            "name": "Belgium",
            "description": "Belgium. ISO 3166-1 BEL / BE / 056. UN member state.",
        },
        "BEN": {
            "name": "Benin",
            "description": "Benin. ISO 3166-1 BEN / BJ / 204. UN member state.",
        },
        "BES": {
            "name": "Bonaire, Sint Eustatius and Saba",
            "description": "Bonaire, Sint Eustatius and Saba. ISO 3166-1 BES / BQ / 535. Sovereignty: Netherlands.",
        },
        "BFA": {
            "name": "Burkina Faso",
            "description": "Burkina Faso. ISO 3166-1 BFA / BF / 854. UN member state.",
        },
        "BGD": {
            "name": "Bangladesh",
            "description": "Bangladesh. ISO 3166-1 BGD / BD / 050. UN member state.",
        },
        "BGR": {
            "name": "Bulgaria",
            "description": "Bulgaria. ISO 3166-1 BGR / BG / 100. UN member state.",
        },
        "BHR": {
            "name": "Bahrain",
            "description": "Bahrain. ISO 3166-1 BHR / BH / 048. UN member state.",
        },
        "BHS": {
            "name": "Bahamas",
            "description": "Bahamas (the). ISO 3166-1 BHS / BS / 044. UN member state.",
        },
        "BIH": {
            "name": "Bosnia and Herzegovina",
            "description": "Bosnia and Herzegovina. ISO 3166-1 BIH / BA / 070. UN member state.",
        },
        "BLM": {
            "name": "Saint Barthélemy",
            "description": "Saint Barthélemy. ISO 3166-1 BLM / BL / 652. Sovereignty: France.",
        },
        "BLR": {
            "name": "Belarus",
            "description": "Belarus. ISO 3166-1 BLR / BY / 112. UN member state.",
        },
        "BLZ": {
            "name": "Belize",
            "description": "Belize. ISO 3166-1 BLZ / BZ / 084. UN member state.",
        },
        "BMU": {
            "name": "Bermuda",
            "description": "Bermuda. ISO 3166-1 BMU / BM / 060. Sovereignty: United Kingdom.",
        },
        "BOL": {
            "name": "Bolivia",
            "description": "Bolivia (Plurinational State of). ISO 3166-1 BOL / BO / 068. UN member state.",
        },
        "BRA": {
            "name": "Brazil",
            "description": "Brazil. ISO 3166-1 BRA / BR / 076. UN member state.",
        },
        "BRB": {
            "name": "Barbados",
            "description": "Barbados. ISO 3166-1 BRB / BB / 052. UN member state.",
        },
        "BRN": {
            "name": "Brunei Darussalam",
            "description": "Brunei Darussalam. ISO 3166-1 BRN / BN / 096. UN member state.",
        },
        "BTN": {
            "name": "Bhutan",
            "description": "Bhutan. ISO 3166-1 BTN / BT / 064. UN member state.",
        },
        "BVT": {
            "name": "Bouvet Island",
            "description": "Bouvet Island. ISO 3166-1 BVT / BV / 074. Sovereignty: Norway.",
        },
        "BWA": {
            "name": "Botswana",
            "description": "Botswana. ISO 3166-1 BWA / BW / 072. UN member state.",
        },
        "CAF": {
            "name": "Central African Republic",
            "description": "Central African Republic (the). ISO 3166-1 CAF / CF / 140. UN member state.",
        },
        "CAN": {
            "name": "Canada",
            "description": "Canada. ISO 3166-1 CAN / CA / 124. UN member state.",
        },
        "CCK": {
            "name": "Cocos (Keeling) Islands",
            "description": "Cocos (Keeling) Islands (the). ISO 3166-1 CCK / CC / 166. Sovereignty: Australia.",
        },
        "CHE": {
            "name": "Switzerland",
            "description": "Switzerland. ISO 3166-1 CHE / CH / 756. UN member state.",
        },
        "CHL": {
            "name": "Chile",
            "description": "Chile. ISO 3166-1 CHL / CL / 152. UN member state.",
        },
        "CHN": {
            "name": "China",
            "description": "China. ISO 3166-1 CHN / CN / 156. UN member state.",
        },
        "CIV": {
            "name": "Côte d'Ivoire",
            "description": "Côte d'Ivoire. ISO 3166-1 CIV / CI / 384. UN member state.",
        },
        "CMR": {
            "name": "Cameroon",
            "description": "Cameroon. ISO 3166-1 CMR / CM / 120. UN member state.",
        },
        "COD": {
            "name": "Democratic Republic of the Congo",
            "description": "Congo (the Democratic Republic of the). ISO 3166-1 COD / CD / 180. UN member state.",
        },
        "COG": {
            "name": "Congo",
            "description": "Congo (the). ISO 3166-1 COG / CG / 178. UN member state.",
        },
        "COK": {
            "name": "Cook Islands",
            "description": "Cook Islands (the). ISO 3166-1 COK / CK / 184. Sovereignty: New Zealand.",
        },
        "COL": {
            "name": "Colombia",
            "description": "Colombia. ISO 3166-1 COL / CO / 170. UN member state.",
        },
        "COM": {
            "name": "Comoros",
            "description": "Comoros (the). ISO 3166-1 COM / KM / 174. UN member state.",
        },
        "CPV": {
            "name": "Cabo Verde",
            "description": "Cabo Verde. ISO 3166-1 CPV / CV / 132. UN member state.",
        },
        "CRI": {
            "name": "Costa Rica",
            "description": "Costa Rica. ISO 3166-1 CRI / CR / 188. UN member state.",
        },
        "CUB": {
            "name": "Cuba",
            "description": "Cuba. ISO 3166-1 CUB / CU / 192. UN member state.",
        },
        "CUW": {
            "name": "Curaçao",
            "description": "Curaçao. ISO 3166-1 CUW / CW / 531. Sovereignty: Netherlands.",
        },
        "CXR": {
            "name": "Christmas Island",
            "description": "Christmas Island. ISO 3166-1 CXR / CX / 162. Sovereignty: Australia.",
        },
        "CYM": {
            "name": "Cayman Islands",
            "description": "Cayman Islands (the). ISO 3166-1 CYM / KY / 136. Sovereignty: United Kingdom.",
        },
        "CYP": {
            "name": "Cyprus",
            "description": "Cyprus. ISO 3166-1 CYP / CY / 196. UN member state.",
        },
        "CZE": {
            "name": "Czechia",
            "description": "Czechia. ISO 3166-1 CZE / CZ / 203. UN member state.",
        },
        "DEU": {
            "name": "Germany",
            "description": "Germany. ISO 3166-1 DEU / DE / 276. UN member state.",
        },
        "DJI": {
            "name": "Djibouti",
            "description": "Djibouti. ISO 3166-1 DJI / DJ / 262. UN member state.",
        },
        "DMA": {
            "name": "Dominica",
            "description": "Dominica. ISO 3166-1 DMA / DM / 212. UN member state.",
        },
        "DNK": {
            "name": "Denmark",
            "description": "Denmark. ISO 3166-1 DNK / DK / 208. UN member state.",
        },
        "DOM": {
            "name": "Dominican Republic",
            "description": "Dominican Republic (the). ISO 3166-1 DOM / DO / 214. UN member state.",
        },
        "DZA": {
            "name": "Algeria",
            "description": "Algeria. ISO 3166-1 DZA / DZ / 012. UN member state.",
        },
        "ECU": {
            "name": "Ecuador",
            "description": "Ecuador. ISO 3166-1 ECU / EC / 218. UN member state.",
        },
        "EGY": {
            "name": "Egypt",
            "description": "Egypt. ISO 3166-1 EGY / EG / 818. UN member state.",
        },
        "ERI": {
            "name": "Eritrea",
            "description": "Eritrea. ISO 3166-1 ERI / ER / 232. UN member state.",
        },
        "ESH": {
            "name": "Western Sahara",
            "description": "Western Sahara. ISO 3166-1 ESH / EH / 732. Sovereignty: Disputed.",
        },
        "ESP": {
            "name": "Spain",
            "description": "Spain. ISO 3166-1 ESP / ES / 724. UN member state.",
        },
        "EST": {
            "name": "Estonia",
            "description": "Estonia. ISO 3166-1 EST / EE / 233. UN member state.",
        },
        "ETH": {
            "name": "Ethiopia",
            "description": "Ethiopia. ISO 3166-1 ETH / ET / 231. UN member state.",
        },
        "FIN": {
            "name": "Finland",
            "description": "Finland. ISO 3166-1 FIN / FI / 246. UN member state.",
        },
        "FJI": {
            "name": "Fiji",
            "description": "Fiji. ISO 3166-1 FJI / FJ / 242. UN member state.",
        },
        "FLK": {
            "name": "Falkland Islands",
            "description": "Falkland Islands (the). ISO 3166-1 FLK / FK / 238. Sovereignty: United Kingdom.",
        },
        "FRA": {
            "name": "France",
            "description": "France. ISO 3166-1 FRA / FR / 250. UN member state.",
        },
        "FRO": {
            "name": "Faroe Islands",
            "description": "Faroe Islands (the). ISO 3166-1 FRO / FO / 234. Sovereignty: Denmark.",
        },
        "FSM": {
            "name": "Micronesia",
            "description": "Micronesia (Federated States of). ISO 3166-1 FSM / FM / 583. UN member state.",
        },
        "GAB": {
            "name": "Gabon",
            "description": "Gabon. ISO 3166-1 GAB / GA / 266. UN member state.",
        },
        "GBR": {
            "name": "United Kingdom",
            "description": "United Kingdom of Great Britain and Northern Ireland (the). ISO 3166-1 GBR / GB / 826. UN member state.",
        },
        "GEO": {
            "name": "Georgia",
            "description": "Georgia. ISO 3166-1 GEO / GE / 268. UN member state.",
        },
        "GGY": {
            "name": "Guernsey",
            "description": "Guernsey. ISO 3166-1 GGY / GG / 831. Sovereignty: British Crown.",
        },
        "GHA": {
            "name": "Ghana",
            "description": "Ghana. ISO 3166-1 GHA / GH / 288. UN member state.",
        },
        "GIB": {
            "name": "Gibraltar",
            "description": "Gibraltar. ISO 3166-1 GIB / GI / 292. Sovereignty: United Kingdom.",
        },
        "GIN": {
            "name": "Guinea",
            "description": "Guinea. ISO 3166-1 GIN / GN / 324. UN member state.",
        },
        "GLP": {
            "name": "Guadeloupe",
            "description": "Guadeloupe. ISO 3166-1 GLP / GP / 312. Sovereignty: France.",
        },
        "GMB": {
            "name": "Gambia",
            "description": "Gambia (the). ISO 3166-1 GMB / GM / 270. UN member state.",
        },
        "GNB": {
            "name": "Guinea-Bissau",
            "description": "Guinea-Bissau. ISO 3166-1 GNB / GW / 624. UN member state.",
        },
        "GNQ": {
            "name": "Equatorial Guinea",
            "description": "Equatorial Guinea. ISO 3166-1 GNQ / GQ / 226. UN member state.",
        },
        "GRC": {
            "name": "Greece",
            "description": "Greece. ISO 3166-1 GRC / GR / 300. UN member state.",
        },
        "GRD": {
            "name": "Grenada",
            "description": "Grenada. ISO 3166-1 GRD / GD / 308. UN member state.",
        },
        "GRL": {
            "name": "Greenland",
            "description": "Greenland. ISO 3166-1 GRL / GL / 304. Sovereignty: Denmark.",
        },
        "GTM": {
            "name": "Guatemala",
            "description": "Guatemala. ISO 3166-1 GTM / GT / 320. UN member state.",
        },
        "GUF": {
            "name": "French Guiana",
            "description": "French Guiana. ISO 3166-1 GUF / GF / 254. Sovereignty: France.",
        },
        "GUM": {
            "name": "Guam",
            "description": "Guam. ISO 3166-1 GUM / GU / 316. Sovereignty: United States.",
        },
        "GUY": {
            "name": "Guyana",
            "description": "Guyana. ISO 3166-1 GUY / GY / 328. UN member state.",
        },
        "HKG": {
            "name": "Hong Kong",
            "description": "Hong Kong. ISO 3166-1 HKG / HK / 344. Sovereignty: China.",
        },
        "HMD": {
            "name": "Heard Island and McDonald Islands",
            "description": "Heard Island and McDonald Islands. ISO 3166-1 HMD / HM / 334. Sovereignty: Australia.",
        },
        "HND": {
            "name": "Honduras",
            "description": "Honduras. ISO 3166-1 HND / HN / 340. UN member state.",
        },
        "HRV": {
            "name": "Croatia",
            "description": "Croatia. ISO 3166-1 HRV / HR / 191. UN member state.",
        },
        "HTI": {
            "name": "Haiti",
            "description": "Haiti. ISO 3166-1 HTI / HT / 332. UN member state.",
        },
        "HUN": {
            "name": "Hungary",
            "description": "Hungary. ISO 3166-1 HUN / HU / 348. UN member state.",
        },
        "IDN": {
            "name": "Indonesia",
            "description": "Indonesia. ISO 3166-1 IDN / ID / 360. UN member state.",
        },
        "IMN": {
            "name": "Isle of Man",
            "description": "Isle of Man. ISO 3166-1 IMN / IM / 833. Sovereignty: British Crown.",
        },
        "IND": {
            "name": "India",
            "description": "India. ISO 3166-1 IND / IN / 356. UN member state.",
        },
        "IOT": {
            "name": "British Indian Ocean Territory",
            "description": "British Indian Ocean Territory (the). ISO 3166-1 IOT / IO / 086. Sovereignty: United Kingdom.",
        },
        "IRL": {
            "name": "Ireland",
            "description": "Ireland. ISO 3166-1 IRL / IE / 372. UN member state.",
        },
        "IRN": {
            "name": "Iran",
            "description": "Iran (Islamic Republic of). ISO 3166-1 IRN / IR / 364. UN member state.",
        },
        "IRQ": {
            "name": "Iraq",
            "description": "Iraq. ISO 3166-1 IRQ / IQ / 368. UN member state.",
        },
        "ISL": {
            "name": "Iceland",
            "description": "Iceland. ISO 3166-1 ISL / IS / 352. UN member state.",
        },
        "ISR": {
            "name": "Israel",
            "description": "Israel. ISO 3166-1 ISR / IL / 376. UN member state.",
        },
        "ITA": {
            "name": "Italy",
            "description": "Italy. ISO 3166-1 ITA / IT / 380. UN member state.",
        },
        "JAM": {
            "name": "Jamaica",
            "description": "Jamaica. ISO 3166-1 JAM / JM / 388. UN member state.",
        },
        "JEY": {
            "name": "Jersey",
            "description": "Jersey. ISO 3166-1 JEY / JE / 832. Sovereignty: British Crown.",
        },
        "JOR": {
            "name": "Jordan",
            "description": "Jordan. ISO 3166-1 JOR / JO / 400. UN member state.",
        },
        "JPN": {
            "name": "Japan",
            "description": "Japan. ISO 3166-1 JPN / JP / 392. UN member state.",
        },
        "KAZ": {
            "name": "Kazakhstan",
            "description": "Kazakhstan. ISO 3166-1 KAZ / KZ / 398. UN member state.",
        },
        "KEN": {
            "name": "Kenya",
            "description": "Kenya. ISO 3166-1 KEN / KE / 404. UN member state.",
        },
        "KGZ": {
            "name": "Kyrgyzstan",
            "description": "Kyrgyzstan. ISO 3166-1 KGZ / KG / 417. UN member state.",
        },
        "KHM": {
            "name": "Cambodia",
            "description": "Cambodia. ISO 3166-1 KHM / KH / 116. UN member state.",
        },
        "KIR": {
            "name": "Kiribati",
            "description": "Kiribati. ISO 3166-1 KIR / KI / 296. UN member state.",
        },
        "KNA": {
            "name": "Saint Kitts and Nevis",
            "description": "Saint Kitts and Nevis. ISO 3166-1 KNA / KN / 659. UN member state.",
        },
        "KOR": {
            "name": "South Korea",
            "description": "Korea (the Republic of). ISO 3166-1 KOR / KR / 410. UN member state.",
        },
        "KWT": {
            "name": "Kuwait",
            "description": "Kuwait. ISO 3166-1 KWT / KW / 414. UN member state.",
        },
        "LAO": {
            "name": "Lao People's Democratic Republic",
            "description": "Lao People's Democratic Republic (the). ISO 3166-1 LAO / LA / 418. UN member state.",
        },
        "LBN": {
            "name": "Lebanon",
            "description": "Lebanon. ISO 3166-1 LBN / LB / 422. UN member state.",
        },
        "LBR": {
            "name": "Liberia",
            "description": "Liberia. ISO 3166-1 LBR / LR / 430. UN member state.",
        },
        "LBY": {
            "name": "Libya",
            "description": "Libya. ISO 3166-1 LBY / LY / 434. UN member state.",
        },
        "LCA": {
            "name": "Saint Lucia",
            "description": "Saint Lucia. ISO 3166-1 LCA / LC / 662. UN member state.",
        },
        "LIE": {
            "name": "Liechtenstein",
            "description": "Liechtenstein. ISO 3166-1 LIE / LI / 438. UN member state.",
        },
        "LKA": {
            "name": "Sri Lanka",
            "description": "Sri Lanka. ISO 3166-1 LKA / LK / 144. UN member state.",
        },
        "LSO": {
            "name": "Lesotho",
            "description": "Lesotho. ISO 3166-1 LSO / LS / 426. UN member state.",
        },
        "LTU": {
            "name": "Lithuania",
            "description": "Lithuania. ISO 3166-1 LTU / LT / 440. UN member state.",
        },
        "LUX": {
            "name": "Luxembourg",
            "description": "Luxembourg. ISO 3166-1 LUX / LU / 442. UN member state.",
        },
        "LVA": {
            "name": "Latvia",
            "description": "Latvia. ISO 3166-1 LVA / LV / 428. UN member state.",
        },
        "MAC": {
            "name": "Macao",
            "description": "Macao. ISO 3166-1 MAC / MO / 446. Sovereignty: China.",
        },
        "MAF": {
            "name": "Saint Martin",
            "description": "Saint Martin (French part). ISO 3166-1 MAF / MF / 663. Sovereignty: France.",
        },
        "MAR": {
            "name": "Morocco",
            "description": "Morocco. ISO 3166-1 MAR / MA / 504. UN member state.",
        },
        "MCO": {
            "name": "Monaco",
            "description": "Monaco. ISO 3166-1 MCO / MC / 492. UN member state.",
        },
        "MDA": {
            "name": "Moldova",
            "description": "Moldova (the Republic of). ISO 3166-1 MDA / MD / 498. UN member state.",
        },
        "MDG": {
            "name": "Madagascar",
            "description": "Madagascar. ISO 3166-1 MDG / MG / 450. UN member state.",
        },
        "MDV": {
            "name": "Maldives",
            "description": "Maldives. ISO 3166-1 MDV / MV / 462. UN member state.",
        },
        "MEX": {
            "name": "Mexico",
            "description": "Mexico. ISO 3166-1 MEX / MX / 484. UN member state.",
        },
        "MHL": {
            "name": "Marshall Islands",
            "description": "Marshall Islands (the). ISO 3166-1 MHL / MH / 584. UN member state.",
        },
        "MKD": {
            "name": "North Macedonia",
            "description": "North Macedonia. ISO 3166-1 MKD / MK / 807. UN member state.",
        },
        "MLI": {
            "name": "Mali",
            "description": "Mali. ISO 3166-1 MLI / ML / 466. UN member state.",
        },
        "MLT": {
            "name": "Malta",
            "description": "Malta. ISO 3166-1 MLT / MT / 470. UN member state.",
        },
        "MMR": {
            "name": "Myanmar",
            "description": "Myanmar. ISO 3166-1 MMR / MM / 104. UN member state.",
        },
        "MNE": {
            "name": "Montenegro",
            "description": "Montenegro. ISO 3166-1 MNE / ME / 499. UN member state.",
        },
        "MNG": {
            "name": "Mongolia",
            "description": "Mongolia. ISO 3166-1 MNG / MN / 496. UN member state.",
        },
        "MNP": {
            "name": "Northern Mariana Islands",
            "description": "Northern Mariana Islands (the). ISO 3166-1 MNP / MP / 580. Sovereignty: United States.",
        },
        "MOZ": {
            "name": "Mozambique",
            "description": "Mozambique. ISO 3166-1 MOZ / MZ / 508. UN member state.",
        },
        "MRT": {
            "name": "Mauritania",
            "description": "Mauritania. ISO 3166-1 MRT / MR / 478. UN member state.",
        },
        "MSR": {
            "name": "Montserrat",
            "description": "Montserrat. ISO 3166-1 MSR / MS / 500. Sovereignty: United Kingdom.",
        },
        "MTQ": {
            "name": "Martinique",
            "description": "Martinique. ISO 3166-1 MTQ / MQ / 474. Sovereignty: France.",
        },
        "MUS": {
            "name": "Mauritius",
            "description": "Mauritius. ISO 3166-1 MUS / MU / 480. UN member state.",
        },
        "MWI": {
            "name": "Malawi",
            "description": "Malawi. ISO 3166-1 MWI / MW / 454. UN member state.",
        },
        "MYS": {
            "name": "Malaysia",
            "description": "Malaysia. ISO 3166-1 MYS / MY / 458. UN member state.",
        },
        "MYT": {
            "name": "Mayotte",
            "description": "Mayotte. ISO 3166-1 MYT / YT / 175. Sovereignty: France.",
        },
        "NAM": {
            "name": "Namibia",
            "description": "Namibia. ISO 3166-1 NAM / NA / 516. UN member state.",
        },
        "NCL": {
            "name": "New Caledonia",
            "description": "New Caledonia. ISO 3166-1 NCL / NC / 540. Sovereignty: France.",
        },
        "NER": {
            "name": "Niger",
            "description": "Niger (the). ISO 3166-1 NER / NE / 562. UN member state.",
        },
        "NFK": {
            "name": "Norfolk Island",
            "description": "Norfolk Island. ISO 3166-1 NFK / NF / 574. Sovereignty: Australia.",
        },
        "NGA": {
            "name": "Nigeria",
            "description": "Nigeria. ISO 3166-1 NGA / NG / 566. UN member state.",
        },
        "NIC": {
            "name": "Nicaragua",
            "description": "Nicaragua. ISO 3166-1 NIC / NI / 558. UN member state.",
        },
        "NIU": {
            "name": "Niue",
            "description": "Niue. ISO 3166-1 NIU / NU / 570. Sovereignty: New Zealand.",
        },
        "NLD": {
            "name": "Netherlands",
            "description": "Netherlands (Kingdom of the). ISO 3166-1 NLD / NL / 528. UN member state.",
        },
        "NOR": {
            "name": "Norway",
            "description": "Norway. ISO 3166-1 NOR / NO / 578. UN member state.",
        },
        "NPL": {
            "name": "Nepal",
            "description": "Nepal. ISO 3166-1 NPL / NP / 524. UN member state.",
        },
        "NRU": {
            "name": "Nauru",
            "description": "Nauru. ISO 3166-1 NRU / NR / 520. UN member state.",
        },
        "NZL": {
            "name": "New Zealand",
            "description": "New Zealand. ISO 3166-1 NZL / NZ / 554. UN member state.",
        },
        "OMN": {
            "name": "Oman",
            "description": "Oman. ISO 3166-1 OMN / OM / 512. UN member state.",
        },
        "PAK": {
            "name": "Pakistan",
            "description": "Pakistan. ISO 3166-1 PAK / PK / 586. UN member state.",
        },
        "PAN": {
            "name": "Panama",
            "description": "Panama. ISO 3166-1 PAN / PA / 591. UN member state.",
        },
        "PCN": {
            "name": "Pitcairn",
            "description": "Pitcairn. ISO 3166-1 PCN / PN / 612. Sovereignty: United Kingdom.",
        },
        "PER": {
            "name": "Peru",
            "description": "Peru. ISO 3166-1 PER / PE / 604. UN member state.",
        },
        "PHL": {
            "name": "Philippines",
            "description": "Philippines (the). ISO 3166-1 PHL / PH / 608. UN member state.",
        },
        "PLW": {
            "name": "Palau",
            "description": "Palau. ISO 3166-1 PLW / PW / 585. UN member state.",
        },
        "PNG": {
            "name": "Papua New Guinea",
            "description": "Papua New Guinea. ISO 3166-1 PNG / PG / 598. UN member state.",
        },
        "POL": {
            "name": "Poland",
            "description": "Poland. ISO 3166-1 POL / PL / 616. UN member state.",
        },
        "PRI": {
            "name": "Puerto Rico",
            "description": "Puerto Rico. ISO 3166-1 PRI / PR / 630. Sovereignty: United States.",
        },
        "PRK": {
            "name": "North Korea",
            "description": "Korea (the Democratic People's Republic of). ISO 3166-1 PRK / KP / 408. UN member state.",
        },
        "PRT": {
            "name": "Portugal",
            "description": "Portugal. ISO 3166-1 PRT / PT / 620. UN member state.",
        },
        "PRY": {
            "name": "Paraguay",
            "description": "Paraguay. ISO 3166-1 PRY / PY / 600. UN member state.",
        },
        "PSE": {
            "name": "Palestine",
            "description": "Palestine, State of. ISO 3166-1 PSE / PS / 275. Sovereignty: UN observer.",
        },
        "PYF": {
            "name": "French Polynesia",
            "description": "French Polynesia. ISO 3166-1 PYF / PF / 258. Sovereignty: France.",
        },
        "QAT": {
            "name": "Qatar",
            "description": "Qatar. ISO 3166-1 QAT / QA / 634. UN member state.",
        },
        "REU": {
            "name": "Réunion",
            "description": "Réunion. ISO 3166-1 REU / RE / 638. Sovereignty: France.",
        },
        "ROU": {
            "name": "Romania",
            "description": "Romania. ISO 3166-1 ROU / RO / 642. UN member state.",
        },
        "RUS": {
            "name": "Russian Federation",
            "description": "Russian Federation (the). ISO 3166-1 RUS / RU / 643. UN member state.",
        },
        "RWA": {
            "name": "Rwanda",
            "description": "Rwanda. ISO 3166-1 RWA / RW / 646. UN member state.",
        },
        "SAU": {
            "name": "Saudi Arabia",
            "description": "Saudi Arabia. ISO 3166-1 SAU / SA / 682. UN member state.",
        },
        "SDN": {
            "name": "Sudan",
            "description": "Sudan (the). ISO 3166-1 SDN / SD / 729. UN member state.",
        },
        "SEN": {
            "name": "Senegal",
            "description": "Senegal. ISO 3166-1 SEN / SN / 686. UN member state.",
        },
        "SGP": {
            "name": "Singapore",
            "description": "Singapore. ISO 3166-1 SGP / SG / 702. UN member state.",
        },
        "SGS": {
            "name": "South Georgia and the South Sandwich Islands",
            "description": "South Georgia and the South Sandwich Islands. ISO 3166-1 SGS / GS / 239. Sovereignty: United Kingdom.",
        },
        "SHN": {
            "name": "Saint Helena, Ascension and Tristan da Cunha",
            "description": "Saint Helena, Ascension and Tristan da Cunha. ISO 3166-1 SHN / SH / 654. Sovereignty: United Kingdom.",
        },
        "SJM": {
            "name": "Svalbard and Jan Mayen",
            "description": "Svalbard and Jan Mayen. ISO 3166-1 SJM / SJ / 744. Sovereignty: Norway.",
        },
        "SLB": {
            "name": "Solomon Islands",
            "description": "Solomon Islands. ISO 3166-1 SLB / SB / 090. UN member state.",
        },
        "SLE": {
            "name": "Sierra Leone",
            "description": "Sierra Leone. ISO 3166-1 SLE / SL / 694. UN member state.",
        },
        "SLV": {
            "name": "El Salvador",
            "description": "El Salvador. ISO 3166-1 SLV / SV / 222. UN member state.",
        },
        "SMR": {
            "name": "San Marino",
            "description": "San Marino. ISO 3166-1 SMR / SM / 674. UN member state.",
        },
        "SOM": {
            "name": "Somalia",
            "description": "Somalia. ISO 3166-1 SOM / SO / 706. UN member state.",
        },
        "SPM": {
            "name": "Saint Pierre and Miquelon",
            "description": "Saint Pierre and Miquelon. ISO 3166-1 SPM / PM / 666. Sovereignty: France.",
        },
        "SRB": {
            "name": "Serbia",
            "description": "Serbia. ISO 3166-1 SRB / RS / 688. UN member state.",
        },
        "SSD": {
            "name": "South Sudan",
            "description": "South Sudan. ISO 3166-1 SSD / SS / 728. UN member state.",
        },
        "STP": {
            "name": "Sao Tome and Principe",
            "description": "Sao Tome and Principe. ISO 3166-1 STP / ST / 678. UN member state.",
        },
        "SUR": {
            "name": "Suriname",
            "description": "Suriname. ISO 3166-1 SUR / SR / 740. UN member state.",
        },
        "SVK": {
            "name": "Slovakia",
            "description": "Slovakia. ISO 3166-1 SVK / SK / 703. UN member state.",
        },
        "SVN": {
            "name": "Slovenia",
            "description": "Slovenia. ISO 3166-1 SVN / SI / 705. UN member state.",
        },
        "SWE": {
            "name": "Sweden",
            "description": "Sweden. ISO 3166-1 SWE / SE / 752. UN member state.",
        },
        "SWZ": {
            "name": "Eswatini",
            "description": "Eswatini. ISO 3166-1 SWZ / SZ / 748. UN member state.",
        },
        "SXM": {
            "name": "Sint Maarten",
            "description": "Sint Maarten (Dutch part). ISO 3166-1 SXM / SX / 534. Sovereignty: Netherlands.",
        },
        "SYC": {
            "name": "Seychelles",
            "description": "Seychelles. ISO 3166-1 SYC / SC / 690. UN member state.",
        },
        "SYR": {
            "name": "Syrian Arab Republic",
            "description": "Syrian Arab Republic (the). ISO 3166-1 SYR / SY / 760. UN member state.",
        },
        "TCA": {
            "name": "Turks and Caicos Islands",
            "description": "Turks and Caicos Islands (the). ISO 3166-1 TCA / TC / 796. Sovereignty: United Kingdom.",
        },
        "TCD": {
            "name": "Chad",
            "description": "Chad. ISO 3166-1 TCD / TD / 148. UN member state.",
        },
        "TGO": {
            "name": "Togo",
            "description": "Togo. ISO 3166-1 TGO / TG / 768. UN member state.",
        },
        "THA": {
            "name": "Thailand",
            "description": "Thailand. ISO 3166-1 THA / TH / 764. UN member state.",
        },
        "TJK": {
            "name": "Tajikistan",
            "description": "Tajikistan. ISO 3166-1 TJK / TJ / 762. UN member state.",
        },
        "TKL": {
            "name": "Tokelau",
            "description": "Tokelau. ISO 3166-1 TKL / TK / 772. Sovereignty: New Zealand.",
        },
        "TKM": {
            "name": "Turkmenistan",
            "description": "Turkmenistan. ISO 3166-1 TKM / TM / 795. UN member state.",
        },
        "TLS": {
            "name": "Timor-Leste",
            "description": "Timor-Leste. ISO 3166-1 TLS / TL / 626. UN member state.",
        },
        "TON": {
            "name": "Tonga",
            "description": "Tonga. ISO 3166-1 TON / TO / 776. UN member state.",
        },
        "TTO": {
            "name": "Trinidad and Tobago",
            "description": "Trinidad and Tobago. ISO 3166-1 TTO / TT / 780. UN member state.",
        },
        "TUN": {
            "name": "Tunisia",
            "description": "Tunisia. ISO 3166-1 TUN / TN / 788. UN member state.",
        },
        "TUR": {
            "name": "Türkiye",
            "description": "Türkiye. ISO 3166-1 TUR / TR / 792. UN member state.",
        },
        "TUV": {
            "name": "Tuvalu",
            "description": "Tuvalu. ISO 3166-1 TUV / TV / 798. UN member state.",
        },
        "TWN": {
            "name": "Taiwan",
            "description": "Taiwan (Province of China). ISO 3166-1 TWN / TW / 158. Sovereignty: Disputed.",
        },
        "TZA": {
            "name": "Tanzania",
            "description": "Tanzania, the United Republic of. ISO 3166-1 TZA / TZ / 834. UN member state.",
        },
        "UGA": {
            "name": "Uganda",
            "description": "Uganda. ISO 3166-1 UGA / UG / 800. UN member state.",
        },
        "UKR": {
            "name": "Ukraine",
            "description": "Ukraine. ISO 3166-1 UKR / UA / 804. UN member state.",
        },
        "UMI": {
            "name": "United States Minor Outlying Islands",
            "description": "United States Minor Outlying Islands (the). ISO 3166-1 UMI / UM / 581. Sovereignty: United States.",
        },
        "URY": {
            "name": "Uruguay",
            "description": "Uruguay. ISO 3166-1 URY / UY / 858. UN member state.",
        },
        "USA": {
            "name": "United States",
            "description": "United States of America (the). ISO 3166-1 USA / US / 840. UN member state.",
        },
        "UZB": {
            "name": "Uzbekistan",
            "description": "Uzbekistan. ISO 3166-1 UZB / UZ / 860. UN member state.",
        },
        "VAT": {
            "name": "Holy See",
            "description": "Holy See (the). ISO 3166-1 VAT / VA / 336. Sovereignty: UN observer.",
        },
        "VCT": {
            "name": "Saint Vincent and the Grenadines",
            "description": "Saint Vincent and the Grenadines. ISO 3166-1 VCT / VC / 670. UN member state.",
        },
        "VEN": {
            "name": "Venezuela",
            "description": "Venezuela (Bolivarian Republic of). ISO 3166-1 VEN / VE / 862. UN member state.",
        },
        "VGB": {
            "name": "British Virgin Islands",
            "description": "Virgin Islands (British). ISO 3166-1 VGB / VG / 092. Sovereignty: United Kingdom.",
        },
        "VIR": {
            "name": "U.S. Virgin Islands",
            "description": "Virgin Islands (U.S.). ISO 3166-1 VIR / VI / 850. Sovereignty: United States.",
        },
        "VNM": {
            "name": "Viet Nam",
            "description": "Viet Nam. ISO 3166-1 VNM / VN / 704. UN member state.",
        },
        "VUT": {
            "name": "Vanuatu",
            "description": "Vanuatu. ISO 3166-1 VUT / VU / 548. UN member state.",
        },
        "WLF": {
            "name": "Wallis and Futuna",
            "description": "Wallis and Futuna. ISO 3166-1 WLF / WF / 876. Sovereignty: France.",
        },
        "WSM": {
            "name": "Samoa",
            "description": "Samoa. ISO 3166-1 WSM / WS / 882. UN member state.",
        },
        "YEM": {
            "name": "Yemen",
            "description": "Yemen. ISO 3166-1 YEM / YE / 887. UN member state.",
        },
        "ZAF": {
            "name": "South Africa",
            "description": "South Africa. ISO 3166-1 ZAF / ZA / 710. UN member state.",
        },
        "ZMB": {
            "name": "Zambia",
            "description": "Zambia. ISO 3166-1 ZMB / ZM / 894. UN member state.",
        },
        "ZWE": {
            "name": "Zimbabwe",
            "description": "Zimbabwe. ISO 3166-1 ZWE / ZW / 716. UN member state.",
        },
    },
    "CreditorType": {
        "OfficialBilateral": {
            "description": (
                "A government or its export credit or development agency "
                "lending bilaterally."
            ),
        },
        "Multilateral": {
            "description": (
                "A multilateral development bank or international financial "
                "institution."
            ),
        },
        "CommercialBank": {
            "description": (
                "A commercial bank or bank syndicate lending on market terms."
            ),
        },
        "CapitalMarkets": {
            "description": (
                "Dispersed bondholders reached through capital markets issuance."
            ),
        },
        "Other": {
            "description": "A creditor not covered by the other categories.",
        },
    },
    "DebtInstrumentType": {
        "Bond": {
            "description": "A long-term marketable debt security.",
        },
        "Note": {
            "description": "A medium-term marketable debt security.",
        },
        "Bill": {
            "description": "A short-term discount security.",
        },
        "Sukuk": {
            "description": "A sharia-compliant certificate of investment.",
        },
        "LoanFacility": {
            "description": "A bilateral or syndicated loan or credit facility.",
        },
        "Other": {
            "description": "An instrument not covered by the other categories.",
        },
    },
    "DebtorType": {
        "CentralGovernment": {
            "description": (
                "The sovereign state itself, including ministries and "
                "treasuries acting for it."
            ),
        },
        "SubSovereign": {
            "name": "Sub-Sovereign",
            "description": (
                "A sub-national government or territory issuing in its own "
                "name (Emirate of Abu Dhabi, Hong Kong SAR)."
            ),
        },
        "CentralBank": {
            "description": "The monetary authority as a distinct legal entity.",
        },
        "StateOwnedEnterprise": {
            "name": "State-Owned Enterprise",
            "description": ("A public corporation owned or controlled by the state."),
        },
        "IssuanceVehicle": {
            "description": (
                "An SPV established to issue on behalf of a public-sector "
                "obligor (Oman Sovereign Sukuk S.A.O.C.)."
            ),
        },
        "Supranational": {
            "description": (
                "A multilateral institution owned by member states (Asian "
                "Development Bank)."
            ),
        },
        "MultiIssuer": {
            "name": "Multi-Issuer",
            "description": (
                "A composite of several issuers filing jointly; constituents "
                "carried as members."
            ),
        },
    },
    "DocumentClass": {
        "Prospectus": {
            "description": (
                "Standalone disclosure document for a specific offer or "
                "listing; readable on its own."
            ),
        },
        "BaseProspectus": {
            "description": (
                "Programme-level disclosure under which individual tranches "
                "are issued later; no tranche pricing."
            ),
        },
        "Supplement": {
            "description": (
                "Amends or updates an existing prospectus or base prospectus."
            ),
        },
        "FinalTerms": {
            "description": (
                "Completes a base prospectus for one tranche; carries the "
                "tranche economics."
            ),
        },
        "FreeWritingProspectus": {
            "description": (
                "SEC Rule 433 offering communications, mostly final pricing "
                "term sheets."
            ),
        },
        "AnnualReport": {
            "description": (
                "Periodic or standing issuer disclosure not tied to a specific offer."
            ),
        },
        "Notice": {
            "description": (
                "Exchange or regulatory announcements about issuers or instruments."
            ),
        },
        "LoanDocumentation": {
            "description": (
                "Loan contracts and related official-lender documentation."
            ),
        },
        "BondContract": {
            "description": "Contracts of bond issuance and administration.",
        },
        "RestructuringDocument": {
            "description": (
                "Documents proposing, executing, or contracting liability management."
            ),
        },
        "Other": {
            "description": "Reviewed and does not fit any class.",
        },
    },
    "DocumentSectionType": {
        "RiskFactors": {
            "description": "Disclosure of risks to investors.",
        },
        "Definitions": {
            "description": "The defined-terms section.",
        },
        "DescriptionOfSecurities": {
            "name": "Description of Securities",
            "description": "Terms and conditions of the securities.",
        },
        "UseOfProceeds": {
            "name": "Use of Proceeds",
            "description": "How the issuer will use the money raised.",
        },
        "Taxation": {
            "description": "Tax treatment disclosure.",
        },
        "PlanOfDistribution": {
            "name": "Plan of Distribution",
            "description": "Underwriting and distribution arrangements.",
        },
        "Other": {
            "description": "A section not covered by the other categories.",
        },
    },
    "EventType": {
        "Settlement": {
            "description": "The issue settles; money and securities move.",
        },
        "InterestPayment": {
            "description": "A scheduled coupon payment.",
        },
        "Default": {
            "description": (
                "An event of default occurs (non-payment, breach, misrepresentation)."
            ),
        },
        "Moratorium": {
            "description": "The sovereign declares a moratorium on payments.",
        },
        "Acceleration": {
            "description": ("Principal is declared immediately due following default."),
        },
        "Restructuring": {
            "description": (
                "A liability management transaction (exchange, amendment, buyback) is executed or settles."
            ),
        },
        "Other": {
            "description": "An occurrence not covered by the other categories.",
        },
    },
    "GoverningLaw": {
        "NewYork": {
            "name": "New York Law",
            "description": "The law of the State of New York.",
        },
        "English": {
            "name": "English Law",
            "description": "The law of England and Wales.",
        },
        "Local": {
            "name": "Local Law",
            "description": "The issuer's own domestic law.",
        },
        "Other": {
            "description": "A governing law not covered by the other categories.",
        },
    },
    "InterestRateType": {
        "Fixed": {
            "description": "Constant coupon over the instrument's life.",
        },
        "Floating": {
            "description": "Coupon resets off a reference rate plus a margin.",
        },
        "ZeroCoupon": {
            "description": "No periodic interest; issued at a discount.",
        },
        "StepUp": {
            "name": "Step-Up",
            "description": "Coupon changes on a predefined schedule.",
        },
        "Other": {
            "description": ("A rate structure not covered by the other categories."),
        },
    },
    "OrganizationRoleCategory": {
        "Obligor": {
            "description": "A party that owes the debt or stands behind it.",
        },
        "Creditor": {
            "description": "A party with a claim to be paid.",
        },
        "Agent": {
            "name": "Agent / Intermediary",
            "description": (
                "A third party administering the issuance or the relationship."
            ),
        },
        "DistributionAndAdvisory": {
            "name": "Distribution and Advisory",
            "description": (
                "A party distributing the securities or advising on the deal."
            ),
        },
    },
    "OrganizationRoleName": {
        "Issuer": {
            "description": "The entity issuing the instrument.",
        },
        "Borrower": {
            "description": "The entity drawing under a loan facility.",
        },
        "Guarantor": {
            "description": "An entity guaranteeing the obligations.",
        },
        "Bondholder": {
            "description": "A holder of the securities.",
        },
        "Lender": {
            "description": "A lender under a facility.",
        },
        "Trustee": {
            "description": (
                "Independent entity acting on behalf of bondholders and "
                "protecting their interests."
            ),
        },
        "FiscalAgent": {
            "description": (
                "Issuer-appointed provider of administrative services for the issue."
            ),
        },
        "PayingAgent": {
            "description": "Makes payments to holders on the issuer's behalf.",
        },
        "Registrar": {
            "description": "Maintains the register of holders.",
        },
        "TransferAgent": {
            "description": ("Processes transfers and exchanges of the securities."),
        },
        "CalculationAgent": {
            "description": ("Determines rates and amounts for variable terms."),
        },
        "ClearingSystem": {
            "description": (
                "Clears and settles the securities (DTC, Euroclear, Clearstream)."
            ),
        },
        "ProcessAgent": {
            "description": (
                "Accepts service of process in the chosen jurisdiction for "
                "the sovereign."
            ),
        },
        "Underwriter": {
            "description": "Purchases and distributes the securities.",
        },
        "LeadManager": {
            "description": "Leads the syndicate for the offering.",
        },
        "ListingAgent": {
            "description": "Handles the exchange listing.",
        },
        "LegalCounsel": {
            "description": ("Law firm advising a party or delivering opinions."),
        },
    },
    "PariPassuType": {
        "Old": {
            "description": (
                "Pre-2014 wording exposed to the ratable-payment "
                "interpretation litigated in the 1990s-2010s."
            ),
        },
        "Enhanced": {
            "description": (
                "Post-2014 wording clarifying equal ranking only, with no "
                "ratable-payment obligation."
            ),
        },
    },
    "PaymentFrequency": {
        "Annual": {
            "description": "Paid once a year.",
        },
        "SemiAnnual": {
            "name": "Semi-Annual",
            "description": "Paid twice a year.",
        },
        "Quarterly": {
            "description": "Paid four times a year.",
        },
        "Monthly": {
            "description": "Paid monthly.",
        },
        "AtMaturity": {
            "description": "Paid once, at maturity.",
        },
        "Other": {
            "description": "A frequency not covered by the other categories.",
        },
    },
    "PersonRoleCategory": {
        "Execution": {
            "description": "A person executing documents.",
        },
        "Representation": {
            "description": ("A person representing or acting for an organization."),
        },
    },
    "PersonRoleName": {
        "Signatory": {
            "description": ("A person signing an agreement on behalf of a party."),
        },
        "AuthorizedRepresentative": {
            "description": "A person authorized to act for a party.",
        },
        "ContactOfficer": {
            "description": ("A named contact for notices or investor communications."),
        },
    },
    "ProvisionType": {
        "Definitions": {
            "description": (
                "Defines terms used in the agreement; the anchor for DefinedTerms."
            ),
        },
        "GoverningLaw": {
            "description": (
                "Selects the legal framework governing interpretation and enforcement."
            ),
        },
        "Jurisdiction": {
            "description": (
                "Specifies which courts hear disputes; often includes "
                "process-agent appointment."
            ),
        },
        "PaymentTerms": {
            "description": (
                "Amount, timing, and mechanics of interest and principal payments."
            ),
        },
        "FacilityCommitment": {
            "name": "Facility / Commitment",
            "description": ("Size and financial terms of a promise to lend."),
        },
        "Drawdown": {
            "name": "Drawdown / Utilization",
            "description": ("When and how a commitment to lend turns into debt."),
        },
        "ConditionsPrecedent": {
            "description": (
                "What must happen before money moves: authority, approvals, "
                "opinions, information."
            ),
        },
        "RepresentationsAndWarranties": {
            "name": "Representations and Warranties",
            "description": (
                "The borrower testifies to key facts and is liable for lies."
            ),
        },
        "Covenant": {
            "description": (
                "A promise by the issuer on financial management, "
                "information, or conduct."
            ),
        },
        "NegativePledge": {
            "description": (
                "Prohibits securing other creditors without securing this "
                "one proportionately."
            ),
        },
        "PariPassu": {
            "description": (
                "Ranking of this claim relative to the issuer's other "
                "comparable obligations."
            ),
        },
        "InformationUndertaking": {
            "description": ("Reporting and disclosure obligations to creditors."),
        },
        "EventsOfDefault": {
            "name": "Events of Default",
            "description": (
                "Tripwires — non-payment, breach, misrepresentation, "
                "moratorium — giving rise to remedies."
            ),
        },
        "CrossDefault": {
            "name": "Cross-Default",
            "description": (
                "A default under other indebtedness constitutes a default here."
            ),
        },
        "Acceleration": {
            "description": (
                "On default, principal can be declared due immediately; "
                "voting rules apply."
            ),
        },
        "CollectiveActionClause": {
            "description": (
                "Binds all holders to a modification approved by a qualified majority."
            ),
        },
        "NonReservedMatterModification": {
            "name": "Non-Reserved Matter Modification",
            "description": "Rules for modifying non-reserved matters.",
        },
        "ReservedMatterModification": {
            "description": (
                "Rules for modifying reserved matters (payment terms and "
                "other protected matters)."
            ),
        },
        "SovereignImmunityWaiver": {
            "description": (
                "The extent to which the sovereign waives immunity from suit "
                "and execution."
            ),
        },
        "Other": {
            "description": "A provision not covered by the other categories.",
        },
    },
    "Seniority": {
        "SeniorUnsecured": {
            "description": "Senior claim with no collateral.",
        },
        "SeniorSecured": {
            "description": "Senior claim backed by collateral.",
        },
        "Subordinated": {
            "description": "Claim ranking behind senior obligations.",
        },
    },
    "SovereignImmunityWaiverType": {
        "Full": {
            "description": "Immunity waived for suit and execution.",
        },
        "No": {
            "description": "No waiver of sovereign immunity.",
        },
        "Selective": {
            "description": (
                "Waived only for specified proceedings, forums, or assets."
            ),
        },
    },
    "VotingAggregationMethod": {
        "SingleSeries": {
            "description": "Votes counted within one series only.",
        },
        "CrossSeriesSingleAggregated": {
            "name": "Cross-Series, Single Aggregated",
            "description": (
                "One aggregate vote across all affected series; typically "
                "conditioned on uniformly applicable treatment."
            ),
        },
        "CrossSeriesTwoTier": {
            "name": "Cross-Series, Two-Tier",
            "description": (
                "An aggregate threshold across all affected series plus a "
                "separate threshold in each series."
            ),
        },
    },
}
