# University Database with descriptions and image URLs
# Using picsum.photos for placeholder images that look professional

UNIVERSITIES = {
    # Indian Universities
    "IIT Bombay": {
        "desc": "Premier engineering institute known for rigorous academics and top placements across tech and research.",
        "location": "Mumbai, India",
        "ranking": "Top 5 in India",
        "image": "https://upload.wikimedia.org/wikipedia/en/1/1d/IIT_Bombay_Logo.svg"
    },
    "IIT Delhi": {
        "desc": "Leading technical institute with strong industry connections and cutting-edge research facilities.",
        "location": "New Delhi, India",
        "ranking": "Top 3 in India",
        "image": "https://upload.wikimedia.org/wikipedia/en/f/f3/IIT_Delhi_logo.svg"
    },
    "BITS Pilani": {
        "desc": "Autonomous private institute famous for flexible curriculum and entrepreneurial culture.",
        "location": "Pilani, Rajasthan",
        "ranking": "Top 10 in India",
        "image": "https://upload.wikimedia.org/wikipedia/en/d/d3/BITS_Pilani-Logo.svg"
    },
    "NIT Trichy": {
        "desc": "Top National Institute of Technology with excellent placement records and research output.",
        "location": "Tiruchirappalli, Tamil Nadu",
        "ranking": "Best NIT in India",
        "image": "https://upload.wikimedia.org/wikipedia/en/8/8a/National_Institute_of_Technology%2C_Tiruchirappalli_Logo.png"
    },
    "IIIT Hyderabad": {
        "desc": "Research-focused institute specializing in IT, ML/AI with strong startup ecosystem.",
        "location": "Hyderabad, India",
        "ranking": "Top IT Institute",
        "image": "https://upload.wikimedia.org/wikipedia/en/a/a7/IIIT_Hyderabad_Logo.svg"
    },
    "AIIMS Delhi": {
        "desc": "India's most prestigious medical institute with world-class healthcare and research.",
        "location": "New Delhi, India",
        "ranking": "#1 Medical in India",
        "image": "https://upload.wikimedia.org/wikipedia/en/a/a4/AIIMS_Delhi_logo.png"
    },
    "CMC Vellore": {
        "desc": "Mission hospital and medical college known for affordable healthcare and ethics.",
        "location": "Vellore, Tamil Nadu",
        "ranking": "Top 5 Medical",
        "image": "https://upload.wikimedia.org/wikipedia/en/c/c0/Christian_Medical_College_%26_Hospital_Vellore_logo.png"
    },
    "JIPMER Puducherry": {
        "desc": "Central government medical institution with excellent clinical exposure.",
        "location": "Puducherry, India",
        "ranking": "Top 10 Medical",
        "image": "https://upload.wikimedia.org/wikipedia/en/5/50/JIPMER_logo.png"
    },
    "IISc Bangalore": {
        "desc": "India's premier research institute for science and engineering with PhD focus.",
        "location": "Bangalore, India",
        "ranking": "#1 Research Institute",
        "image": "https://upload.wikimedia.org/wikipedia/en/9/94/IISc_Bangalore_logo.svg"
    },
    "IIT Madras": {
        "desc": "Top-ranked IIT with strong research parks and industry collaborations.",
        "location": "Chennai, India",
        "ranking": "#1 in NIRF",
        "image": "https://upload.wikimedia.org/wikipedia/en/6/69/IIT_Madras_Logo.svg"
    },
    "ISI Kolkata": {
        "desc": "World-renowned for statistics and mathematics research.",
        "location": "Kolkata, India",
        "ranking": "Best for Statistics",
        "image": "https://upload.wikimedia.org/wikipedia/en/0/07/ISI_logo.png"
    },
    "NID Ahmedabad": {
        "desc": "Premier design institute shaping India's creative industry leaders.",
        "location": "Ahmedabad, India",
        "ranking": "#1 Design School",
        "image": "https://upload.wikimedia.org/wikipedia/en/4/42/National_Institute_of_Design_logo.svg"
    },
    "IIM Ahmedabad": {
        "desc": "India's top business school with exceptional entrepreneurship culture.",
        "location": "Ahmedabad, India",
        "ranking": "#1 B-School India",
        "image": "https://upload.wikimedia.org/wikipedia/en/5/55/IIM_Ahmedabad_logo.svg"
    },
    "NLSIU Bangalore": {
        "desc": "Pioneer of 5-year law program, producing top legal professionals.",
        "location": "Bangalore, India",
        "ranking": "#1 Law School",
        "image": "https://upload.wikimedia.org/wikipedia/en/8/81/National_Law_School_of_India_University_Logo.png"
    },
    "JNU": {
        "desc": "Jawaharlal Nehru University - Known for social sciences and research.",
        "location": "New Delhi, India",
        "ranking": "Top for Arts/Humanities",
        "image": "https://upload.wikimedia.org/wikipedia/en/4/44/JNU_Logo.png"
    },
    "Delhi University": {
        "desc": "Historic central university with numerous prestigious colleges.",
        "location": "New Delhi, India",
        "ranking": "Top Central University",
        "image": "https://upload.wikimedia.org/wikipedia/en/6/6c/DU_Logo.png"
    },
    "IARI New Delhi": {
        "desc": "Indian Agricultural Research Institute - Premier for agricultural sciences.",
        "location": "New Delhi, India",
        "ranking": "#1 Agriculture",
        "image": "https://upload.wikimedia.org/wikipedia/en/7/74/IARI_logo.png"
    },
    
    # Abroad Universities
    "MIT (USA)": {
        "desc": "Massachusetts Institute of Technology - World's top tech university with groundbreaking research.",
        "location": "Cambridge, Massachusetts, USA",
        "ranking": "#1 Globally (Tech)",
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/0c/MIT_logo.svg"
    },
    "Stanford University (USA)": {
        "desc": "Silicon Valley's university - birthplace of Google, HP, and countless startups.",
        "location": "Stanford, California, USA",
        "ranking": "#3 Globally",
        "image": "https://upload.wikimedia.org/wikipedia/en/b/b4/Stanford_University_Seal.svg"
    },
    "Harvard (USA)": {
        "desc": "World's most prestigious university with unmatched alumni network and resources.",
        "location": "Cambridge, Massachusetts, USA",
        "ranking": "#1 Globally",
        "image": "https://upload.wikimedia.org/wikipedia/en/2/29/Harvard_shield_wreath.svg"
    },
    "Oxford (UK)": {
        "desc": "Oldest English-speaking university with tutorial-based learning system.",
        "location": "Oxford, England",
        "ranking": "#1 in UK",
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Oxford-University-Circlet.svg"
    },
    "Cambridge (UK)": {
        "desc": "Historic university producing Nobel laureates across sciences and humanities.",
        "location": "Cambridge, England",
        "ranking": "#2 in UK",
        "image": "https://upload.wikimedia.org/wikipedia/commons/c/c3/U_of_Cambridge_coat_of_arms.svg"
    },
    "ETH Zurich (Switzerland)": {
        "desc": "Europe's leading science and technology university, Einstein's alma mater.",
        "location": "Zurich, Switzerland",
        "ranking": "#1 in Continental Europe",
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/63/ETH_Zurich_Logo.svg"
    },
    "Carnegie Mellon (USA)": {
        "desc": "Best for Computer Science, AI, and Robotics with strong industry ties.",
        "location": "Pittsburgh, Pennsylvania, USA",
        "ranking": "#1 for CS",
        "image": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Carnegie_Mellon_wordmark.svg"
    },
    "UC Berkeley (USA)": {
        "desc": "Top public university with exceptional research and Silicon Valley access.",
        "location": "Berkeley, California, USA",
        "ranking": "#1 Public University",
        "image": "https://upload.wikimedia.org/wikipedia/commons/a/a1/Seal_of_University_of_California%2C_Berkeley.svg"
    },
    "London School of Economics (UK)": {
        "desc": "World leader in social sciences, economics, and political science.",
        "location": "London, England",
        "ranking": "#1 for Economics",
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/51/LSE_Logo.svg"
    },
    "Wharton (USA)": {
        "desc": "World's first business school, top for finance and entrepreneurship.",
        "location": "Philadelphia, Pennsylvania, USA",
        "ranking": "#1 Business School",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/31/UPenn_shield_with_banner.svg"
    },
    "Harvard Medical School (USA)": {
        "desc": "Premier medical school with affiliated hospitals leading medical innovation.",
        "location": "Boston, Massachusetts, USA",
        "ranking": "#1 Medical School",
        "image": "https://upload.wikimedia.org/wikipedia/en/2/29/Harvard_shield_wreath.svg"
    },
    "Johns Hopkins (USA)": {
        "desc": "Pioneer in research medicine with renowned hospital and public health school.",
        "location": "Baltimore, Maryland, USA",
        "ranking": "Top 3 Medical",
        "image": "https://upload.wikimedia.org/wikipedia/en/5/55/Johns_Hopkins_University_Logo.svg"
    }
}

# Function to get university info
def get_university_info(uni_name):
    """Get university information, returns default if not found"""
    if uni_name in UNIVERSITIES:
        return UNIVERSITIES[uni_name]
    else:
        # Create a basic entry for universities not in database
        return {
            "desc": f"A reputed institution known for quality education in this field.",
            "location": "Check official website",
            "ranking": "Top ranked",
            "image": None
        }
