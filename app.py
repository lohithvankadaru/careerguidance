import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Career Navigator", page_icon="🧭", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button {
        background-color: #4CAF50; color: white;
        font-size: 16px; padding: 10px; border-radius: 10px;
    }
    .stButton>button:hover { background-color: #45a049; }
    .career-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px; border-radius: 15px; text-align: center;
        color: white; margin: 10px 0; cursor: pointer;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .career-icon { font-size: 50px; margin-bottom: 10px; }
    .career-title { font-size: 18px; font-weight: bold; }
    .career-desc { font-size: 12px; opacity: 0.9; }
    .company-card {
        background: white; padding: 15px; border-radius: 10px;
        border-left: 4px solid #4CAF50; margin: 10px 0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .salary-badge {
        background: #e8f5e9; color: #2e7d32; padding: 5px 10px;
        border-radius: 5px; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MAIN TITLE ---
st.title("🚀 Career Navigator")
st.markdown("### Discover your future based on your personality, skills, and dreams.")
st.divider()

# --- SESSION STATE ---
if "step" not in st.session_state:
    st.session_state.step = 1
if "careers" not in st.session_state:
    st.session_state.careers = []
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "selected_career" not in st.session_state:
    st.session_state.selected_career = None

# --- OPTIONS ---
SUBJECT_OPTIONS = ["Math", "English", "Physics", "Chemistry", "Biology", "History", 
                   "Geography", "Civics", "Economics", "Art", "Physical Education", "Coding", "Robotics",
                   "Agriculture", "Business Studies", "Political Science", "Photography", "Environmental Science"]
QUALITY_OPTIONS = ["Leadership", "Empathy", "Analytical Thinking", "Creativity", "Communication", 
                   "Problem Solving", "Teamwork", "Adaptability", "Attention to Detail", "Critical Thinking", 
                   "Patience", "Curiosity", "Risk Taking", "Public Speaking", "Networking", "Self-Discipline", "Negotiation"]

# Experience and Achievement Options
EXPERIENCE_OPTIONS = [
    "🖥️ Coding projects or hackathons",
    "🔬 Science fair or research projects",
    "🎨 Art exhibitions or design work",
    "📰 Writing for school magazine/blog",
    "🏆 Sports competitions or athletics",
    "🎭 Drama, music, or cultural events",
    "📊 Business plan competitions",
    "🌱 Volunteering or social work",
    "💼 Internship at a company",
    "👥 Student council or leadership roles",
    "📸 Photography or videography projects",
    "🌾 Farming or gardening experience",
    "💰 Part-time job or freelancing",
    "🗣️ Debate or public speaking competitions"
]

# Map experiences to careers
EXPERIENCE_TO_CAREERS = {
    "🖥️ Coding projects or hackathons": ["Software Developer", "Data Scientist", "Robotics Engineer"],
    "🔬 Science fair or research projects": ["Doctor", "Professor", "Environmental Scientist", "Data Scientist"],
    "🎨 Art exhibitions or design work": ["Graphic Designer", "Architect"],
    "📰 Writing for school magazine/blog": ["Journalist", "Photo Journalist", "Teacher", "Professor"],
    "🏆 Sports competitions or athletics": ["Athlete / Sports Coach"],
    "🎭 Drama, music, or cultural events": ["Teacher", "Politician"],
    "📊 Business plan competitions": ["Entrepreneur", "Financial Advisor", "Economist"],
    "🌱 Volunteering or social work": ["Doctor", "Civil Servant (IAS/IPS)", "Teacher", "Politician"],
    "💼 Internship at a company": ["Software Developer", "Data Scientist", "Financial Advisor"],
    "👥 Student council or leadership roles": ["Civil Servant (IAS/IPS)", "Politician", "Entrepreneur"],
    "📸 Photography or videography projects": ["Photo Journalist", "Graphic Designer"],
    "🌾 Farming or gardening experience": ["Organic Farmer"],
    "💰 Part-time job or freelancing": ["Entrepreneur", "Financial Advisor", "Graphic Designer"],
    "🗣️ Debate or public speaking competitions": ["Lawyer", "Politician", "Civil Servant (IAS/IPS)"]
}

# Motivation Factor Options with realistic data
MOTIVATION_OPTIONS = [
    "💰 High Salary (Avg ₹25-50 LPA for top performers)",
    "🔬 Scientific Discovery & Research (Impact millions through innovation)",
    "🎨 Creative Expression (Design, art, building things)",
    "🌍 Social Impact (Help communities, change lives)",
    "🚀 Innovation & Entrepreneurship (Build your own venture)",
    "📈 Career Growth (Fast promotions, leadership roles)",
    "⚖️ Work-Life Balance (Flexible hours, remote work)",
    "🏆 Fame & Recognition (Public figure, thought leader)",
    "🔒 Job Security (Stable government/PSU jobs)",
    "🌱 Sustainability & Environment (Protect the planet)"
]

# Map motivations to careers (weight: 5 - very high priority)
MOTIVATION_TO_CAREERS = {
    "💰 High Salary (Avg ₹25-50 LPA for top performers)": ["Software Developer", "Data Scientist", "Financial Advisor", "Lawyer", "Doctor"],
    "🔬 Scientific Discovery & Research (Impact millions through innovation)": ["Doctor", "Professor", "Data Scientist", "Robotics Engineer"],
    "🎨 Creative Expression (Design, art, building things)": ["Graphic Designer", "Architect", "Photo Journalist"],
    "🌍 Social Impact (Help communities, change lives)": ["Doctor", "Teacher", "Civil Servant (IAS/IPS)", "Politician", "Organic Farmer"],
    "🚀 Innovation & Entrepreneurship (Build your own venture)": ["Entrepreneur", "Software Developer", "Robotics Engineer"],
    "📈 Career Growth (Fast promotions, leadership roles)": ["Software Developer", "Financial Advisor", "Civil Servant (IAS/IPS)", "Lawyer"],
    "⚖️ Work-Life Balance (Flexible hours, remote work)": ["Graphic Designer", "Teacher", "Photo Journalist", "Professor"],
    "🏆 Fame & Recognition (Public figure, thought leader)": ["Politician", "Athlete / Sports Coach", "Photo Journalist", "Entrepreneur"],
    "🔒 Job Security (Stable government/PSU jobs)": ["Civil Servant (IAS/IPS)", "Teacher", "Professor", "Doctor"],
    "🌱 Sustainability & Environment (Protect the planet)": ["Organic Farmer", "Architect"]
}

# --- CAREER DATABASE ---
CAREERS = {
    "Software Developer": {
        "icon": "💻", "desc": "Design and build software applications and systems",
        "subjects": ["Math", "Coding", "Physics"],
        "qualities": ["Analytical Thinking", "Problem Solving", "Creativity"],
        "courses": ["B.Tech Computer Science", "BCA", "Online Bootcamps (Coursera, Udemy)", "M.Tech Software Engineering"],
        "universities_india": ["IIT Bombay", "IIT Delhi", "BITS Pilani", "NIT Trichy", "IIIT Hyderabad"],
        "universities_abroad": ["MIT (USA)", "Stanford University (USA)", "Carnegie Mellon (USA)", "ETH Zurich (Switzerland)", "University of Cambridge (UK)"],
        "salary": {"entry": "₹4-8 LPA", "mid": "₹12-20 LPA", "senior": "₹25-50 LPA"},
        "companies": [
            {"name": "Google", "desc": "World's leading tech company known for search, cloud, and AI products", "entry_salary": "₹15-25 LPA"},
            {"name": "Microsoft", "desc": "Global software giant behind Windows, Azure, and Office suite", "entry_salary": "₹12-20 LPA"},
            {"name": "Amazon", "desc": "E-commerce and cloud computing leader with AWS services", "entry_salary": "₹12-18 LPA"},
            {"name": "TCS", "desc": "India's largest IT services company with global presence", "entry_salary": "₹4-7 LPA"},
            {"name": "Infosys", "desc": "Leading Indian multinational IT consulting company", "entry_salary": "₹4-6 LPA"}
        ]
    },
    "Doctor": {
        "icon": "🩺", "desc": "Diagnose and treat patients to improve health and save lives",
        "subjects": ["Biology", "Chemistry", "Physics"],
        "qualities": ["Empathy", "Patience", "Attention to Detail", "Communication"],
        "courses": ["MBBS (5.5 years)", "MD/MS Specialization", "NEET Entrance Exam", "Super-specialization (DM/MCh)"],
        "universities_india": ["AIIMS Delhi", "CMC Vellore", "JIPMER Puducherry", "Armed Forces Medical College", "Maulana Azad Medical College"],
        "universities_abroad": ["Harvard Medical School (USA)", "Johns Hopkins (USA)", "Oxford University (UK)", "University of Melbourne (Australia)", "Karolinska Institute (Sweden)"],
        "salary": {"entry": "₹8-15 LPA", "mid": "₹20-40 LPA", "senior": "₹50-1 Cr+"},
        "companies": [
            {"name": "AIIMS Hospitals", "desc": "Premier government medical institutes with cutting-edge research", "entry_salary": "₹80K-1L/month"},
            {"name": "Apollo Hospitals", "desc": "India's largest private healthcare chain with 70+ hospitals", "entry_salary": "₹60K-1L/month"},
            {"name": "Fortis Healthcare", "desc": "Leading private hospital network across India", "entry_salary": "₹50K-80K/month"},
            {"name": "Max Healthcare", "desc": "Premium hospital chain known for advanced treatments", "entry_salary": "₹55K-90K/month"},
            {"name": "Medanta", "desc": "World-class multi-specialty hospital founded by renowned surgeons", "entry_salary": "₹60K-1L/month"}
        ]
    },
    "Data Scientist": {
        "icon": "📊", "desc": "Analyze complex data to extract insights and drive decisions",
        "subjects": ["Math", "Coding", "Economics"],
        "qualities": ["Analytical Thinking", "Critical Thinking", "Curiosity", "Problem Solving"],
        "courses": ["B.Tech + M.Tech in Data Science", "MSc Statistics", "Online certifications (Coursera, edX)", "PhD in Machine Learning"],
        "universities_india": ["IISc Bangalore", "IIT Madras", "ISI Kolkata", "IIT Kharagpur", "IIIT Hyderabad"],
        "universities_abroad": ["MIT (USA)", "Stanford (USA)", "UC Berkeley (USA)", "ETH Zurich (Switzerland)", "University of Toronto (Canada)"],
        "salary": {"entry": "₹6-12 LPA", "mid": "₹18-35 LPA", "senior": "₹40-80 LPA"},
        "companies": [
            {"name": "Google", "desc": "Leading AI/ML research with DeepMind and Google Brain teams", "entry_salary": "₹18-30 LPA"},
            {"name": "Meta", "desc": "Social media giant investing heavily in AI and metaverse", "entry_salary": "₹20-35 LPA"},
            {"name": "Flipkart", "desc": "India's e-commerce leader using data for personalization", "entry_salary": "₹15-25 LPA"},
            {"name": "Amazon", "desc": "Uses data science for recommendations, logistics, and AWS", "entry_salary": "₹15-25 LPA"},
            {"name": "Mu Sigma", "desc": "World's largest pure-play analytics company based in India", "entry_salary": "₹6-10 LPA"}
        ]
    },
    "Architect": {
        "icon": "🏛️", "desc": "Design buildings that are functional, safe, and aesthetically pleasing",
        "subjects": ["Art", "Math", "Physics"],
        "qualities": ["Creativity", "Attention to Detail", "Problem Solving", "Communication"],
        "courses": ["B.Arch (5 years)", "M.Arch", "NATA Entrance Exam", "Sustainable Design Certifications"],
        "universities_india": ["IIT Kharagpur", "SPA Delhi", "CEPT Ahmedabad", "NIT Trichy", "JJ School of Architecture Mumbai"],
        "universities_abroad": ["Harvard GSD (USA)", "MIT (USA)", "AA School London (UK)", "TU Delft (Netherlands)", "ETH Zurich (Switzerland)"],
        "salary": {"entry": "₹4-8 LPA", "mid": "₹12-25 LPA", "senior": "₹30-60 LPA"},
        "companies": [
            {"name": "Hafeez Contractor", "desc": "India's most prolific architect with 1000+ projects", "entry_salary": "₹4-7 LPA"},
            {"name": "RSP Architects", "desc": "Singapore-based firm with major projects across Asia", "entry_salary": "₹5-8 LPA"},
            {"name": "Gensler", "desc": "World's largest architecture firm with global presence", "entry_salary": "₹6-10 LPA"},
            {"name": "Foster + Partners", "desc": "British firm known for iconic sustainable buildings", "entry_salary": "₹7-12 LPA"},
            {"name": "DLF Design", "desc": "Real estate giant's in-house architecture division", "entry_salary": "₹5-8 LPA"}
        ]
    },
    "Graphic Designer": {
        "icon": "🎨", "desc": "Create visual content for brands, websites, and marketing",
        "subjects": ["Art", "Coding", "English"],
        "qualities": ["Creativity", "Attention to Detail", "Communication", "Adaptability"],
        "courses": ["BFA Graphic Design", "B.Des Communication Design", "Adobe Certifications", "UI/UX Bootcamps"],
        "universities_india": ["NID Ahmedabad", "Srishti Bangalore", "MIT Institute of Design Pune", "Pearl Academy", "NIFT"],
        "universities_abroad": ["Rhode Island School of Design (USA)", "Parsons New York (USA)", "Royal College of Art (UK)", "ArtCenter College (USA)", "Central Saint Martins (UK)"],
        "salary": {"entry": "₹3-6 LPA", "mid": "₹8-15 LPA", "senior": "₹18-35 LPA"},
        "companies": [
            {"name": "Ogilvy", "desc": "Global advertising giant with creative excellence", "entry_salary": "₹4-7 LPA"},
            {"name": "Dentsu", "desc": "Japanese creative network with global reach", "entry_salary": "₹4-6 LPA"},
            {"name": "Adobe", "desc": "Creator of industry-standard design software", "entry_salary": "₹10-15 LPA"},
            {"name": "Canva", "desc": "Australian design platform revolutionizing graphic design", "entry_salary": "₹8-12 LPA"},
            {"name": "Razorpay", "desc": "Fintech unicorn with strong design culture", "entry_salary": "₹6-10 LPA"}
        ]
    },
    "Teacher": {
        "icon": "📚", "desc": "Educate and inspire students to learn and grow",
        "subjects": ["English", "History", "Civics"],
        "qualities": ["Patience", "Communication", "Empathy", "Leadership"],
        "courses": ["B.Ed (Bachelor of Education)", "M.Ed", "CTET/TET Exams", "Subject-specific Masters"],
        "universities_india": ["Delhi University", "Jamia Millia Islamia", "BHU Varanasi", "TISS Mumbai", "Azim Premji University"],
        "universities_abroad": ["Harvard Graduate School of Education (USA)", "Stanford Education (USA)", "UCL Institute of Education (UK)", "University of Melbourne (Australia)", "University of Toronto (Canada)"],
        "salary": {"entry": "₹3-6 LPA", "mid": "₹8-15 LPA", "senior": "₹15-30 LPA"},
        "companies": [
            {"name": "Delhi Public School", "desc": "India's largest chain of private schools", "entry_salary": "₹4-7 LPA"},
            {"name": "Kendriya Vidyalaya", "desc": "Government schools for central govt employees' children", "entry_salary": "₹45K-60K/month"},
            {"name": "BYJU'S", "desc": "India's largest edtech company with online learning", "entry_salary": "₹5-10 LPA"},
            {"name": "Unacademy", "desc": "Popular online learning platform for competitive exams", "entry_salary": "₹4-8 LPA"},
            {"name": "International Schools", "desc": "IB/Cambridge curriculum schools with global standards", "entry_salary": "₹6-12 LPA"}
        ]
    },
    "Robotics Engineer": {
        "icon": "🤖", "desc": "Design and build robots and automated systems",
        "subjects": ["Robotics", "Coding", "Math", "Physics"],
        "qualities": ["Problem Solving", "Creativity", "Analytical Thinking", "Curiosity"],
        "courses": ["B.Tech Robotics/Mechatronics", "M.Tech Automation", "ROS Certifications", "AI/ML Courses"],
        "universities_india": ["IIT Kanpur", "IIT Bombay", "BITS Pilani", "VIT Vellore", "Manipal Institute of Technology"],
        "universities_abroad": ["Carnegie Mellon Robotics (USA)", "MIT (USA)", "ETH Zurich (Switzerland)", "Imperial College London (UK)", "University of Tokyo (Japan)"],
        "salary": {"entry": "₹5-10 LPA", "mid": "₹15-30 LPA", "senior": "₹35-70 LPA"},
        "companies": [
            {"name": "Boston Dynamics", "desc": "World leader in dynamic robots like Spot and Atlas", "entry_salary": "$80K-120K"},
            {"name": "Tesla", "desc": "Electric vehicle company with advanced automation", "entry_salary": "$90K-130K"},
            {"name": "ISRO", "desc": "India's space agency using robotics for missions", "entry_salary": "₹8-12 LPA"},
            {"name": "ABB Robotics", "desc": "Global leader in industrial robotics and automation", "entry_salary": "₹6-10 LPA"},
            {"name": "DRDO", "desc": "Defense research using robotics for military applications", "entry_salary": "₹8-12 LPA"}
        ]
    },
    "Lawyer": {
        "icon": "⚖️", "desc": "Represent clients in legal matters and advocate for justice",
        "subjects": ["Civics", "English", "History"],
        "qualities": ["Communication", "Critical Thinking", "Analytical Thinking", "Leadership"],
        "courses": ["5-year Integrated LLB", "3-year LLB after graduation", "LLM Specialization", "Bar Council Enrollment"],
        "universities_india": ["NLSIU Bangalore", "NALSAR Hyderabad", "NLU Delhi", "NUJS Kolkata", "ILS Pune"],
        "universities_abroad": ["Harvard Law School (USA)", "Yale Law School (USA)", "Oxford University (UK)", "Cambridge University (UK)", "Columbia Law School (USA)"],
        "salary": {"entry": "₹5-12 LPA", "mid": "₹20-50 LPA", "senior": "₹1-5 Cr+"},
        "companies": [
            {"name": "AZB & Partners", "desc": "India's largest law firm with corporate expertise", "entry_salary": "₹15-20 LPA"},
            {"name": "Cyril Amarchand Mangaldas", "desc": "Leading full-service law firm in India", "entry_salary": "₹15-18 LPA"},
            {"name": "Khaitan & Co", "desc": "One of India's oldest and most prestigious law firms", "entry_salary": "₹12-16 LPA"},
            {"name": "Trilegal", "desc": "Top-tier Indian law firm known for M&A deals", "entry_salary": "₹12-15 LPA"},
            {"name": "Supreme Court", "desc": "Highest court of India - prestigious litigation practice", "entry_salary": "₹3-10 LPA (varies)"}
        ]
    },
    "Athlete / Sports Coach": {
        "icon": "🏆", "desc": "Compete professionally or train athletes for peak performance",
        "subjects": ["Physical Education", "Biology", "Math"],
        "qualities": ["Leadership", "Teamwork", "Patience", "Adaptability"],
        "courses": ["B.P.Ed", "M.P.Ed", "Sports Science Degree", "Coaching Certifications (NIS)"],
        "universities_india": ["LNIPE Gwalior", "SAI Training Centers", "Symbiosis Sports", "Amity Sports", "KIIT Bhubaneswar"],
        "universities_abroad": ["Loughborough University (UK)", "University of Florida (USA)", "Australian Institute of Sport", "German Sport University Cologne", "University of Oregon (USA)"],
        "salary": {"entry": "₹2-5 LPA", "mid": "₹8-25 LPA", "senior": "₹30 LPA - Crores"},
        "companies": [
            {"name": "Sports Authority of India", "desc": "Government body for sports development and training", "entry_salary": "₹4-8 LPA"},
            {"name": "IPL Teams", "desc": "Indian Premier League cricket franchises", "entry_salary": "₹20L - Crores"},
            {"name": "Pro Kabaddi Teams", "desc": "Professional kabaddi league teams across India", "entry_salary": "₹10L-50L"},
            {"name": "JSW Sports", "desc": "Corporate sports initiative supporting Indian athletes", "entry_salary": "₹4-10 LPA"},
            {"name": "Reliance Foundation", "desc": "Supports grassroots sports development programs", "entry_salary": "₹4-8 LPA"}
        ]
    },
    "Economist": {
        "icon": "📈", "desc": "Study economic trends and advise on financial policies",
        "subjects": ["Economics", "Math", "History"],
        "qualities": ["Analytical Thinking", "Critical Thinking", "Communication", "Curiosity"],
        "courses": ["BA/MA Economics", "MSc Econometrics", "PhD Economics", "CFA Certification"],
        "universities_india": ["Delhi School of Economics", "JNU", "ISI Kolkata", "Gokhale Institute Pune", "IIM Bangalore"],
        "universities_abroad": ["MIT (USA)", "Harvard (USA)", "London School of Economics (UK)", "Princeton (USA)", "University of Chicago (USA)"],
        "salary": {"entry": "₹6-12 LPA", "mid": "₹18-35 LPA", "senior": "₹40-80 LPA"},
        "companies": [
            {"name": "RBI", "desc": "India's central bank managing monetary policy", "entry_salary": "₹8-15 LPA"},
            {"name": "World Bank", "desc": "International organization funding development projects", "entry_salary": "$60K-100K"},
            {"name": "IMF", "desc": "Global financial stability organization", "entry_salary": "$70K-110K"},
            {"name": "McKinsey", "desc": "Top consulting firm with economic advisory", "entry_salary": "₹20-30 LPA"},
            {"name": "NITI Aayog", "desc": "India's policy think tank advising government", "entry_salary": "₹8-15 LPA"}
        ]
    },
    "Organic Farmer": {
        "icon": "🌾", "desc": "Grow crops using sustainable and chemical-free farming methods",
        "subjects": ["Agriculture", "Biology", "Environmental Science", "Chemistry"],
        "qualities": ["Patience", "Self-Discipline", "Problem Solving", "Adaptability"],
        "courses": ["BSc Agriculture", "MSc Organic Farming", "Permaculture Certifications", "Agricultural Extension Diplomas"],
        "universities_india": ["IARI New Delhi", "Tamil Nadu Agricultural University", "Punjab Agricultural University", "UAS Bangalore", "GB Pant University"],
        "universities_abroad": ["Wageningen University (Netherlands)", "UC Davis (USA)", "University of Reading (UK)", "Lincoln University (New Zealand)", "Swedish University of Agricultural Sciences"],
        "salary": {"entry": "₹2-5 LPA", "mid": "₹8-15 LPA", "senior": "₹20-50 LPA (farm owners)"},
        "companies": [
            {"name": "24 Mantra Organic", "desc": "India's leading organic food brand with 50,000+ farmers", "entry_salary": "₹3-5 LPA"},
            {"name": "Organic India", "desc": "Premium organic products company promoting sustainable farming", "entry_salary": "₹3-6 LPA"},
            {"name": "Big Basket (Fresho)", "desc": "Online grocery with organic produce sourcing", "entry_salary": "₹3-5 LPA"},
            {"name": "Sresta Natural Bioproducts", "desc": "Organic farming consultancy and product company", "entry_salary": "₹3-5 LPA"},
            {"name": "Own Farm Business", "desc": "Start your own organic farm - potential earnings based on scale", "entry_salary": "Variable"}
        ]
    },
    "Financial Advisor": {
        "icon": "💵", "desc": "Help individuals and businesses manage money and investments",
        "subjects": ["Economics", "Math", "Business Studies"],
        "qualities": ["Analytical Thinking", "Communication", "Networking", "Attention to Detail", "Negotiation"],
        "courses": ["BCom/MCom", "MBA Finance", "CFP Certification", "CFA Charter", "NISM Certifications"],
        "universities_india": ["IIM Ahmedabad", "IIM Bangalore", "XLRI Jamshedpur", "FMS Delhi", "SP Jain Mumbai"],
        "universities_abroad": ["Wharton (USA)", "London Business School (UK)", "INSEAD (France)", "Columbia Business School (USA)", "NYU Stern (USA)"],
        "salary": {"entry": "₹4-8 LPA", "mid": "₹12-25 LPA", "senior": "₹30-1 Cr+ (with commissions)"},
        "companies": [
            {"name": "HDFC Bank Wealth", "desc": "India's leading private bank wealth management division", "entry_salary": "₹5-8 LPA"},
            {"name": "ICICI Prudential", "desc": "Major insurance and investment company", "entry_salary": "₹4-7 LPA"},
            {"name": "Kotak Wealth Management", "desc": "Premium wealth advisory for HNI clients", "entry_salary": "₹6-10 LPA"},
            {"name": "Axis Bank Priority", "desc": "Priority banking and financial planning services", "entry_salary": "₹5-8 LPA"},
            {"name": "Zerodha/Groww", "desc": "Fintech platforms for retail investors", "entry_salary": "₹6-12 LPA"}
        ]
    },
    "Photo Journalist": {
        "icon": "📸", "desc": "Capture powerful images that tell news stories and document events",
        "subjects": ["Photography", "English", "History", "Civics"],
        "qualities": ["Creativity", "Curiosity", "Adaptability", "Communication", "Risk Taking"],
        "courses": ["BA Journalism", "Diploma in Photojournalism", "Mass Communication Degree", "Photography Workshops"],
        "universities_india": ["AJK Mass Communication (JMI)", "IIMC Delhi", "Xavier Institute of Communications", "Symbiosis (SIMC)", "Asian College of Journalism"],
        "universities_abroad": ["Missouri School of Journalism (USA)", "Columbia Journalism School (USA)", "Cardiff University (UK)", "Sydney University (Australia)", "Goldsmiths London (UK)"],
        "salary": {"entry": "₹3-6 LPA", "mid": "₹8-15 LPA", "senior": "₹20-40 LPA (freelance potential higher)"},
        "companies": [
            {"name": "Reuters", "desc": "Global news agency with award-winning photo division", "entry_salary": "₹6-12 LPA"},
            {"name": "Associated Press (AP)", "desc": "World's oldest news agency with photo services", "entry_salary": "₹5-10 LPA"},
            {"name": "The Hindu", "desc": "Leading Indian newspaper with strong photojournalism", "entry_salary": "₹4-7 LPA"},
            {"name": "Getty Images", "desc": "World's largest visual media company", "entry_salary": "₹5-10 LPA"},
            {"name": "National Geographic", "desc": "Iconic magazine known for stunning photography", "entry_salary": "$40K-70K"}
        ]
    },
    "Professor": {
        "icon": "🎓", "desc": "Teach at universities and conduct advanced research in your field",
        "subjects": ["English", "Math", "Physics", "Chemistry", "Biology", "History", "Economics"],
        "qualities": ["Patience", "Communication", "Curiosity", "Critical Thinking", "Leadership"],
        "courses": ["Masters in Subject", "PhD (Mandatory)", "NET/SET Qualification", "Post-doctoral Research"],
        "universities_india": ["IITs", "IIMs", "Central Universities", "NITs", "IISc Bangalore"],
        "universities_abroad": ["Harvard (USA)", "Oxford (UK)", "MIT (USA)", "Cambridge (UK)", "Stanford (USA)"],
        "salary": {"entry": "₹8-15 LPA (Assistant Prof)", "mid": "₹15-25 LPA (Associate Prof)", "senior": "₹25-40 LPA (Full Professor)"},
        "companies": [
            {"name": "IITs", "desc": "India's premier engineering institutes with top research", "entry_salary": "₹12-18 LPA"},
            {"name": "Central Universities", "desc": "Government universities across India", "entry_salary": "₹8-12 LPA"},
            {"name": "Private Universities", "desc": "Ashoka, Shiv Nadar, Azim Premji - growing private sector", "entry_salary": "₹10-20 LPA"},
            {"name": "IIMs", "desc": "Top business schools - highly competitive positions", "entry_salary": "₹20-35 LPA"},
            {"name": "Research Institutes", "desc": "TIFR, NCBS, IISC for pure research careers", "entry_salary": "₹10-18 LPA"}
        ]
    },
    "Entrepreneur": {
        "icon": "🚀", "desc": "Start and grow your own business to solve problems and create value",
        "subjects": ["Business Studies", "Economics", "Coding", "Math"],
        "qualities": ["Risk Taking", "Leadership", "Creativity", "Networking", "Problem Solving", "Adaptability"],
        "courses": ["BBA/MBA", "Startup Incubator Programs", "Online Business Courses", "Industry Experience"],
        "universities_india": ["IIM Ahmedabad (CIIE)", "IIT Bombay (SINE)", "ISB Hyderabad", "BITS Pilani", "NSRCEL Bangalore"],
        "universities_abroad": ["Stanford (USA)", "MIT Sloan (USA)", "Harvard Business School (USA)", "INSEAD (France)", "London Business School (UK)"],
        "salary": {"entry": "Negative to ₹0 (Investment phase)", "mid": "Variable (Revenue phase)", "senior": "₹1 Cr - ₹1000 Cr+ (Success phase)"},
        "companies": [
            {"name": "Y Combinator", "desc": "World's top startup accelerator (3% acceptance)", "entry_salary": "$500K investment"},
            {"name": "Sequoia Surge", "desc": "India-focused early stage startup program", "entry_salary": "$1-2M seed funding"},
            {"name": "Venture Highway", "desc": "Early stage VC backing Indian startups", "entry_salary": "Seed funding"},
            {"name": "100X.VC", "desc": "Indian VC with founder-friendly approach", "entry_salary": "₹1.25 Cr for 5%"},
            {"name": "Startup India Hub", "desc": "Government initiative supporting new businesses", "entry_salary": "Grants & support"}
        ]
    },
    "Civil Servant (IAS/IPS)": {
        "icon": "🏛️", "desc": "Serve the nation through administrative and policy roles in government",
        "subjects": ["Political Science", "History", "Geography", "Civics", "Economics"],
        "qualities": ["Leadership", "Communication", "Critical Thinking", "Empathy", "Self-Discipline"],
        "courses": ["Any Graduate Degree", "UPSC CSE Preparation", "Optional Subject Mastery", "Interview Preparation"],
        "universities_india": ["LBSNAA Mussoorie (Training)", "Delhi University", "JNU", "St. Stephen's College", "Loyola College Chennai"],
        "universities_abroad": ["Not typically required - Indian exam focused", "Oxford/Cambridge for further study", "Harvard Kennedy School", "LSE", "Sciences Po Paris"],
        "salary": {"entry": "₹8-12 LPA (+ perks)", "mid": "₹15-25 LPA (+ housing, car)", "senior": "₹25-40 LPA (Cabinet Secretary level)"},
        "companies": [
            {"name": "Indian Administrative Service", "desc": "Steel frame of India - district to central govt roles", "entry_salary": "₹56,100/month + DA + perks"},
            {"name": "Indian Police Service", "desc": "Lead police forces from SP to DGP level", "entry_salary": "₹56,100/month + DA + perks"},
            {"name": "Indian Foreign Service", "desc": "Represent India as diplomats worldwide", "entry_salary": "₹56,100/month + postings abroad"},
            {"name": "Indian Revenue Service", "desc": "Tax administration and policy", "entry_salary": "₹56,100/month + DA"},
            {"name": "State Civil Services", "desc": "State-level administrative positions", "entry_salary": "₹40,000-60,000/month (varies by state)"}
        ]
    },
    "Politician": {
        "icon": "🗳️", "desc": "Represent people, make laws, and shape public policy through elected office",
        "subjects": ["Political Science", "History", "Civics", "Economics", "English"],
        "qualities": ["Leadership", "Public Speaking", "Networking", "Empathy", "Negotiation", "Adaptability"],
        "courses": ["Any Degree (Law/Political Science preferred)", "Public Policy courses", "Leadership programs", "Ground-level party work"],
        "universities_india": ["Delhi University", "JNU (Political Science)", "Symbiosis Law School", "NLSIU Bangalore", "Ashoka University"],
        "universities_abroad": ["Oxford PPE (UK)", "Harvard Kennedy School (USA)", "LSE (UK)", "Sciences Po (France)", "Georgetown (USA)"],
        "salary": {"entry": "₹0-2 LPA (Party worker)", "mid": "₹5-15 LPA (MLA salary)", "senior": "₹20-40 LPA (MP/Minister salary)"},
        "companies": [
            {"name": "Indian National Congress", "desc": "Grand Old Party - one of India's oldest political parties", "entry_salary": "Voluntary/Variable"},
            {"name": "Bharatiya Janata Party", "desc": "Currently ruling party with largest membership", "entry_salary": "Voluntary/Variable"},
            {"name": "Aam Aadmi Party", "desc": "New-age party focused on governance", "entry_salary": "Voluntary/Variable"},
            {"name": "Regional Parties", "desc": "DMK, TMC, SP, BSP - strong state presence", "entry_salary": "Voluntary/Variable"},
            {"name": "Independent Politics", "desc": "Contest as independent candidate", "entry_salary": "Self-funded"}
        ]
    }
}

# --- MATCHING FUNCTION ---
def match_careers(subjects, qualities, experiences=None, motivations=None):
    scores = {}
    for name, data in CAREERS.items():
        score = 0
        # Subject matching (weight: 3)
        score += sum(3 for s in subjects if s in data["subjects"])
        # Quality matching (weight: 2)
        score += sum(2 for q in qualities if q in data["qualities"])
        # Experience matching (weight: 4)
        if experiences:
            for exp in experiences:
                if exp in EXPERIENCE_TO_CAREERS:
                    if name in EXPERIENCE_TO_CAREERS[exp]:
                        score += 4
        # Motivation matching (weight: 5 - highest priority!)
        if motivations:
            for mot in motivations:
                if mot in MOTIVATION_TO_CAREERS:
                    if name in MOTIVATION_TO_CAREERS[mot]:
                        score += 5  # Highest weight for motivation match
        if score > 0:
            scores[name] = score
    sorted_careers = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [c[0] for c in sorted_careers[:5]]

# --- PROGRESS BAR ---
total_steps = 7
if st.session_state.step <= total_steps:
    st.progress(st.session_state.step / total_steps)
    st.markdown(f"**Question {st.session_state.step} of {total_steps}**")
elif st.session_state.step == 8:
    st.progress(1.0)
    st.markdown("**✅ Survey Complete - Select Your Career!**")
else:
    st.progress(1.0)
    st.markdown("**🎯 Career Details**")
st.divider()

# --- NAVIGATION ---
def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1

# --- QUESTIONS ---
if st.session_state.step == 1:
    st.subheader("1️⃣ What is your name?")
    name = st.text_input("Name", value=st.session_state.answers.get("name", ""), label_visibility="collapsed")
    if st.button("Next ➡️"):
        if name:
            st.session_state.answers["name"] = name
            next_step(); st.rerun()
        else: st.error("Please enter your name")

elif st.session_state.step == 2:
    st.subheader("2️⃣ What are your favourite subjects?")
    subjects = st.multiselect("Subjects", SUBJECT_OPTIONS, default=st.session_state.answers.get("subjects", []), label_visibility="collapsed")
    c1, c2 = st.columns(2)
    if c1.button("⬅️ Back"): prev_step(); st.rerun()
    if c2.button("Next ➡️"):
        if subjects:
            st.session_state.answers["subjects"] = subjects
            next_step(); st.rerun()
        else: st.error("Select at least one subject")

elif st.session_state.step == 3:
    st.subheader("3️⃣ What are your personal qualities?")
    qualities = st.multiselect("Qualities", QUALITY_OPTIONS, default=st.session_state.answers.get("qualities", []), label_visibility="collapsed")
    c1, c2 = st.columns(2)
    if c1.button("⬅️ Back"): prev_step(); st.rerun()
    if c2.button("Next ➡️"):
        if qualities:
            st.session_state.answers["qualities"] = qualities
            next_step(); st.rerun()
        else: st.error("Select at least one quality")

elif st.session_state.step == 4:
    st.markdown("### 4️⃣ 🏆 Work Experience & Past Achievements")
    st.markdown("*Select all experiences and achievements that apply to you:*")
    
    prev_exp = st.session_state.answers.get("experiences", [])
    experiences = st.multiselect(
        "Select your experiences",
        options=EXPERIENCE_OPTIONS,
        default=prev_exp,
        label_visibility="collapsed"
    )
    
    c1, c2 = st.columns(2)
    if c1.button("⬅️ Back"): prev_step(); st.rerun()
    if c2.button("Next ➡️"):
        st.session_state.answers["experiences"] = experiences
        next_step(); st.rerun()

elif st.session_state.step == 5:
    st.subheader("5️⃣ Do you want to study abroad?")
    abroad = st.radio("Study Abroad", ["Yes", "No", "Maybe"], index=["Yes", "No", "Maybe"].index(st.session_state.answers.get("study_abroad", "Yes")), label_visibility="collapsed")
    c1, c2 = st.columns(2)
    if c1.button("⬅️ Back"): prev_step(); st.rerun()
    if c2.button("Next ➡️"):
        st.session_state.answers["study_abroad"] = abroad
        next_step(); st.rerun()

elif st.session_state.step == 6:
    st.markdown("### 6️⃣ 🎯 What motivates you the most in a career?")
    st.markdown("*Select the factors that are most important to you (realistic data shown):*")
    
    prev_mot = st.session_state.answers.get("motivations", [])
    motivations = st.multiselect(
        "Select your motivations",
        options=MOTIVATION_OPTIONS,
        default=prev_mot,
        label_visibility="collapsed"
    )
    
    c1, c2 = st.columns(2)
    if c1.button("⬅️ Back"): prev_step(); st.rerun()
    if c2.button("Next ➡️"):
        if motivations:
            st.session_state.answers["motivations"] = motivations
            next_step(); st.rerun()
        else: st.error("Select at least one motivation")

elif st.session_state.step == 7:
    st.subheader("7️⃣ What impact do you want to make?")
    impact = st.text_area("Impact", value=st.session_state.answers.get("impact", ""), placeholder="E.g., Help people, innovate technology, protect environment...", label_visibility="collapsed")
    c1, c2 = st.columns(2)
    if c1.button("⬅️ Back"): prev_step(); st.rerun()
    if c2.button("🎯 Find My Careers"):
        st.session_state.answers["impact"] = impact if impact else "Make a positive difference"
        st.session_state.careers = match_careers(
            st.session_state.answers.get("subjects", []), 
            st.session_state.answers.get("qualities", []),
            st.session_state.answers.get("experiences", []),
            st.session_state.answers.get("motivations", [])
        )
        if not st.session_state.careers:
            st.session_state.careers = ["Software Developer", "Teacher", "Graphic Designer"]
        st.session_state.step = 8; st.rerun()

# --- STEP 8: CAREER SELECTION ---
elif st.session_state.step == 8:
    st.balloons()
    st.subheader(f"🎉 Hi {st.session_state.answers.get('name', 'there')}! Here are your top career matches:")
    st.markdown("*Click on a career to see detailed information*")
    
    cols = st.columns(len(st.session_state.careers))
    for i, career in enumerate(st.session_state.careers):
        with cols[i]:
            data = CAREERS.get(career, {"icon": "💼", "desc": "Exciting career opportunity"})
            st.markdown(f"""
            <div class="career-card">
                <div class="career-icon">{data['icon']}</div>
                <div class="career-title">{career}</div>
                <div class="career-desc">{data['desc']}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Select {career.split()[0]}", key=f"select_{i}"):
                st.session_state.selected_career = career
                st.session_state.step = 9
                st.rerun()
    
    st.markdown("---")
    if st.button("🔄 Start Over"):
        st.session_state.step = 1
        st.session_state.careers = []
        st.session_state.answers = {}
        st.session_state.selected_career = None
        st.rerun()

# --- STEP 9: CAREER DETAILS ---
elif st.session_state.step == 9:
    career = st.session_state.selected_career
    data = CAREERS.get(career, {})
    answers = st.session_state.answers
    
    st.markdown(f"# {data.get('icon', '💼')} {career}")
    st.markdown(f"*{data.get('desc', '')}*")
    st.divider()
    
    # COURSES
    st.markdown("## 📚 Recommended Courses")
    for course in data.get("courses", []):
        st.markdown(f"- {course}")
    
    st.divider()
    
    # UNIVERSITIES
    st.markdown("## 🎓 Best Universities")
    
    # Import university data
    from universities import get_university_info
    
    # Indian Universities
    st.markdown("### 🇮🇳 Universities in India")
    uni_cols = st.columns(3)
    for idx, uni in enumerate(data.get("universities_india", [])):
        uni_info = get_university_info(uni)
        with uni_cols[idx % 3]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); 
                        padding: 15px; border-radius: 12px; margin: 8px 0; min-height: 150px;
                        box-shadow: 0 3px 10px rgba(0,0,0,0.1);">
                <h4 style="margin: 0 0 8px 0; color: #1a365d;">🏛️ {uni}</h4>
                <p style="font-size: 12px; color: #4a5568; margin: 5px 0;">{uni_info['desc']}</p>
                <p style="font-size: 11px; color: #718096; margin: 3px 0;">📍 {uni_info['location']}</p>
                <span style="background: #48bb78; color: white; padding: 3px 8px; border-radius: 10px; font-size: 10px;">
                    {uni_info['ranking']}
                </span>
            </div>
            """, unsafe_allow_html=True)
    
    # Abroad Universities
    if answers.get("study_abroad") in ["Yes", "Maybe"]:
        st.markdown("### 🌍 Universities Abroad")
        abroad_cols = st.columns(3)
        for idx, uni in enumerate(data.get("universities_abroad", [])):
            uni_info = get_university_info(uni)
            with abroad_cols[idx % 3]:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                            padding: 15px; border-radius: 12px; margin: 8px 0; min-height: 150px;
                            box-shadow: 0 3px 10px rgba(0,0,0,0.15);">
                    <h4 style="margin: 0 0 8px 0; color: white;">🌐 {uni}</h4>
                    <p style="font-size: 12px; color: rgba(255,255,255,0.9); margin: 5px 0;">{uni_info['desc']}</p>
                    <p style="font-size: 11px; color: rgba(255,255,255,0.8); margin: 3px 0;">📍 {uni_info['location']}</p>
                    <span style="background: rgba(255,255,255,0.2); color: white; padding: 3px 8px; border-radius: 10px; font-size: 10px;">
                        {uni_info['ranking']}
                    </span>
                </div>
                """, unsafe_allow_html=True)
    
    st.divider()
    
    # SALARY
    st.markdown("## 💰 Salary Expectations")
    sal = data.get("salary", {})
    c1, c2, c3 = st.columns(3)
    c1.metric("Entry Level", sal.get("entry", "N/A"))
    c2.metric("Mid Level", sal.get("mid", "N/A"))
    c3.metric("Senior Level", sal.get("senior", "N/A"))
    
    st.divider()
    
    # COMPANIES
    st.markdown("## 🏢 Top Companies to Work For")
    for comp in data.get("companies", []):
        st.markdown(f"""
        <div class="company-card">
            <strong style="font-size:18px;">{comp['name']}</strong>
            <p style="color:#666; margin:5px 0;">{comp['desc']}</p>
            <span class="salary-badge">Entry Salary: {comp['entry_salary']}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    c1, c2 = st.columns(2)
    if c1.button("⬅️ Back to Careers"):
        st.session_state.step = 8
        st.rerun()
    if c2.button("🔄 Start Over"):
        st.session_state.step = 1
        st.session_state.careers = []
        st.session_state.answers = {}
        st.session_state.selected_career = None
        st.rerun()