import json
import base64
import os

scratch_path = r'C:\Users\Enter Computer\.gemini\antigravity\scratch\abdelaziz-portfolio'
downloads_path = r'C:\Users\Enter Computer\Downloads'

def get_base64(path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('utf-8')
    return ''

profile_b64 = get_base64(os.path.join(scratch_path, 'public', 'assets', 'profile.jpg'))
steam_b64 = get_base64(os.path.join(scratch_path, 'public', 'assets', 'dashboard_steam.jpg'))
cost_b64 = get_base64(os.path.join(scratch_path, 'public', 'assets', 'dashboard_cost.jpg'))
misuo_b64 = get_base64(os.path.join(scratch_path, 'public', 'assets', 'dashboard_misuo.jpg'))

with open(os.path.join(scratch_path, 'src', 'data', 'steam_data.json'), 'r', encoding='utf-8') as f:
    steam_data = json.load(f)

with open(os.path.join(scratch_path, 'src', 'data', 'cost_data.json'), 'r', encoding='utf-8') as f:
    cost_data = json.load(f)

with open(os.path.join(scratch_path, 'src', 'data', 'misuo_data.json'), 'r', encoding='utf-8') as f:
    misuo_data = json.load(f)

template = """<!DOCTYPE html>
<html lang="en" dir="ltr" data-theme="dark" class="dark scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Abdelaziz Osama Mahmoud | Senior Data Analyst & BI Specialist</title>

  <!-- Anti-flicker script for Theme Persistence -->
  <script>
    (function() {
      try {
        var savedTheme = localStorage.getItem('portfolio_theme');
        if (savedTheme === 'light') {
          document.documentElement.setAttribute('data-theme', 'light');
          document.documentElement.classList.remove('dark');
        } else {
          document.documentElement.setAttribute('data-theme', 'dark');
          document.documentElement.classList.add('dark');
        }
      } catch (e) {}
    })();
  </script>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            cairo: ['Cairo', 'sans-serif'],
            sans: ['Plus Jakarta Sans', 'sans-serif']
          }
        }
      }
    }
  </script>

  <!-- React & ReactDOM CDN -->
  <script src="https://unpkg.com/react@18/umd/react.production.min.js" crossorigin></script>
  <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js" crossorigin></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>

  <!-- Chart.js CDN -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

  <style>
    /* CSS Variables for Modern Electric Blue & Navy Dual Theme System */
    :root, [data-theme="dark"], html.dark {
      --bg-main: #071225;
      --bg-secondary: #0B1730;
      --bg-nav: #081329;
      --bg-card: #101F3B;
      --bg-elevated: #152747;
      --border-muted: #233B61;
      --text-primary: #F5F8FF;
      --text-secondary: #B8C7DF;
      --text-muted: #8FA4C4;
      --accent-primary: #3B82F6;
      --accent-bright: #60A5FA;
      --accent-hover: #2563EB;
      --accent-light: rgba(59, 130, 246, 0.16);
      --accent-contrast: #FFFFFF;
      --bg-hover: #182C52;
      --shadow-color: rgba(0, 0, 0, 0.45);
      --glow-shadow: 0 0 20px rgba(59, 130, 246, 0.25);
    }

    [data-theme="light"], html:not(.dark)[data-theme="light"] {
      --bg-main: #F5F8FF;
      --bg-secondary: #EAF1FF;
      --bg-nav: #FFFFFF;
      --bg-card: #FFFFFF;
      --bg-elevated: #F0F5FF;
      --border-muted: #D8E3F5;
      --text-primary: #14213D;
      --text-secondary: #475569;
      --text-muted: #64748B;
      --accent-primary: #2563EB;
      --accent-bright: #3B82F6;
      --accent-hover: #1D4ED8;
      --accent-light: rgba(59, 130, 246, 0.08);
      --accent-contrast: #FFFFFF;
      --bg-hover: #E2ECFE;
      --shadow-color: rgba(20, 33, 61, 0.08);
      --glow-shadow: 0 0 15px rgba(37, 99, 235, 0.15);
    }

    * {
      transition: background-color 0.25s ease, border-color 0.25s ease, color 0.25s ease, box-shadow 0.25s ease;
    }

    body {
      background-color: var(--bg-main);
      color: var(--text-primary);
      margin: 0;
      padding: 0;
    }

    /* Core Theme Helper Classes */
    .theme-bg-main { background-color: var(--bg-main); }
    .theme-bg-secondary { background-color: var(--bg-secondary); }
    .theme-bg-nav { background-color: var(--bg-nav); }
    .theme-bg-card { background-color: var(--bg-card); }
    .theme-bg-elevated { background-color: var(--bg-elevated); }
    .theme-border { border-color: var(--border-muted); }
    
    .theme-text-primary { color: var(--text-primary); }
    .theme-text-secondary { color: var(--text-secondary); }
    .theme-text-muted { color: var(--text-muted); }
    .theme-text-accent { color: var(--accent-primary); }
    .theme-text-bright { color: var(--accent-bright); }

    .theme-bg-accent { background-color: var(--accent-primary); color: var(--accent-contrast); }
    .theme-bg-accent:hover { background-color: var(--accent-hover); }
    .theme-bg-accent-light { background-color: var(--accent-light); }

    .theme-hover-bg:hover { background-color: var(--bg-hover); }
    .theme-glow { box-shadow: var(--glow-shadow); }

    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: var(--bg-main); }
    ::-webkit-scrollbar-thumb { background: var(--border-muted); border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: var(--accent-primary); }
  </style>
</head>
<body>
  <div id="root"></div>

  <script type="text/babel">
    const { useState, useEffect, useRef } = React;

    const profileImg = "__PROFILE_B64__";
    const steamImg = "__STEAM_B64__";
    const costImg = "__COST_B64__";
    const misuoImg = "__MISUO_B64__";

    const steamData = __STEAM_DATA__;
    const costData = __COST_DATA__;
    const misuoData = __MISUO_DATA__;

    const portfolioContent = {
      en: {
        personal: {
          name: "Abdelaziz Osama Mahmoud",
          title: "Senior Data Analyst & Business Intelligence Specialist",
          subtitle: "Cost Accountant & Operational Analytics Lead",
          tagline: "Transforming complex operational & financial data into executive strategic dashboards and profitable business decisions.",
          bio: "Senior Data Analyst & BI Specialist with advanced expertise combining Cost Accounting, Manufacturing Operations, and E-Commerce Supply Chain Logistics with Business Intelligence. Proven track record in building executive interactive dashboards, quantity variance models, SLA delivery performance, and big-data game market intelligence.",
          email: "abdelaziz.osama.analytics@gmail.com",
          phone: "+20 100 000 0000",
          location: "Cairo, Egypt",
          linkedin: "https://linkedin.com/in/abdelaziz-osama-data",
          linkedinDisplay: "linkedin.com/in/abdelaziz-osama-data",
          github: "https://github.com/abdelaziz-data",
          resumePdf: "Abdelaziz Usama Mahmoud Abdelaziz Resume.pdf"
        },
        contactSection: {
          title: "Contact Information",
          subtitle: "I'm actively looking for opportunities to apply my accounting, data analytics, and business intelligence expertise. Feel free to reach out with any questions or collaboration opportunities.",
          formName: "Your Name",
          formEmail: "Your Email",
          formSubject: "Subject",
          formMessage: "Message",
          placeholderName: "John Doe",
          placeholderEmail: "john@example.com",
          placeholderSubject: "Job Opportunity / Project Inquiry",
          placeholderMessage: "Tell me about your project or opportunity...",
          sendBtn: "Send Message",
          sentBtn: "Message Sent Successfully!"
        },
        stats: [
          { label: "Data Records Analyzed", value: "22,524", suffix: "Titles" },
          { label: "Steam Concurrent Players", value: "5.7M+", suffix: "CCU" },
          { label: "E-Commerce Revenue Modeled", value: "1.29M", suffix: "EGP" },
          { label: "Production Units Tracked", value: "465K+", suffix: "Units" }
        ],
        skills: [
          { 
            category: "Business Intelligence & Data Analytics", 
            items: ["Power BI & DAX Modeling", "Power Query & ETL Pipelines", "Data Architecture", "Python (Pandas, NumPy)", "SQL Database Querying", "Executive Dashboard Design"] 
          },
          { 
            category: "Financial & Cost Accounting", 
            items: ["Quantity Variance Analysis", "Product Cost Allocation", "Financial Modeling & Pricing", "Budgeting & Forecasting", "Managerial Reporting", "Excel Visual Reports & VBA"] 
          },
          { 
            category: "Operations & E-Commerce Logistics BI", 
            items: ["On-Time Delivery (SLA)", "Sales Channel Distribution", "Inventory & Storage Analytics", "Regional Demand Mapping", "Order Cancellation Analysis", "Supply Chain Optimization"] 
          }
        ],
        projects: [
          {
            id: "steam-analytics",
            title: "Steam Gaming Industry Market Intelligence & Player Engagement Analysis",
            category: "Big Data & Market Analytics",
            badge: "Power BI & Excel Report",
            image: steamImg,
            excelFile: "Database.xlsx",
            description: "Comprehensive analytical study of 22,524 game titles on Steam, tracking 5.7M+ concurrent users (CCU), sentiment breakdown, platform OS distribution (Windows, Mac, Linux), and free vs paid monetization models.",
            highlights: [
              "Monitored 5,705,135 concurrent players across global Steam titles.",
              "86.0% overall positive review sentiment ratio vs 14.0% negative feedback.",
              "Analyzed platform compatibility: Windows leads at 99.9%, Mac at 27%, Linux at 18%.",
              "Identified top gaming titles driven by CS:GO, PUBG, Elden Ring, and Rust."
            ]
          },
          {
            id: "cost-variance",
            title: "Manufacturing Production Capacity & Quantity Variance Analysis",
            category: "Cost Accounting & Operations",
            badge: "Production Order Visual Report",
            image: costImg,
            excelFile: "Production Order Visual Report.xlsx",
            description: "Executive cost accounting dashboard tracking 465,165 production capacity units across cosmetics & personal care brands. Features granular quantity variance isolation (3,657 units) and top revenue-generating SKUs.",
            highlights: [
              "Tracked total production capacity of 465,165 units across active work orders.",
              "Isolated 3,657 unit quantity variance and identified top 10 variance SKUs.",
              "Highlighted top revenue generators led by Black Hair Wax 1000g (86,384 EGP).",
              "Categorized production orders across 18 brands (Senor leading with 141 orders, Leven with 98)."
            ]
          },
          {
            id: "misuo-ecommerce",
            title: "MISUO E-Commerce Sales & Supply Chain Delivery Performance BI",
            category: "E-Commerce & Supply Chain BI",
            badge: "MISUO Executive Dashboard",
            image: misuoImg,
            excelFile: "MISUO - Abdelaziz Usama Mahmoud.xlsx",
            description: "End-to-end sales and delivery fulfillment dashboard analyzing 1,292,886 EGP total sales across 152 orders. Evaluates regional governorate demand, retail sales channels, and delivery SLA success rates.",
            highlights: [
              "Analyzed 1.29M EGP total revenue with an average order value of 10,261 EGP.",
              "Cairo governorate led regional demand with 60 orders, followed by Giza (24) and Qalyubia (11).",
              "Sales channel breakdown: HomeMart platform led with 94 items sold.",
              "Evaluated delivery performance: 81% successfully delivered, 18% cancelled/refused."
            ]
          }
        ]
      },
      ar: {
        personal: {
          name: "عبدالعزيز أسامة محمود",
          title: "محلل بيانات أول ومختص الذكاء التجاري (BI Specialist)",
          subtitle: "محاسب تكاليف ومسؤول تحليلات العمليات الصناعية",
          tagline: "تحويل البيانات المبعثرة والمعقدة إلى قرارات استراتيجية مربحة ولوحات قيادة تفاعلية مذهلة.",
          bio: "محلل بيانات محترف ذو خبرة متقدمة في ربط التحليل المالي وتحليل التكاليف بذكاء الأعمال (Business Intelligence). متمكن في تصميم وتطوير لوحات القيادة التفاعلية لتتبع الأداء المالي والإنتاجي، وتحليل انحراف الكميات والتكاليف الصناعية، وتتبع سلاسل الإمداد ومبيعات التجارة الإلكترونية.",
          email: "abdelaziz.osama.analytics@gmail.com",
          phone: "+20 100 000 0000",
          location: "القاهرة، مصر",
          linkedin: "https://linkedin.com/in/abdelaziz-osama-data",
          linkedinDisplay: "linkedin.com/in/abdelaziz-osama-data",
          github: "https://github.com/abdelaziz-data",
          resumePdf: "Abdelaziz Usama Mahmoud Abdelaziz Resume.pdf"
        },
        contactSection: {
          title: "معلومات التواصل",
          subtitle: "أبحث بنشاط عن فرص متميزة لتطبيق خبراتي في تحليل البيانات والذكاء التجاري ومحاسبة التكاليف. يسعدني تواصلك لأي استفسارات أو فرص عمل أو مشاريع مشتركة.",
          formName: "الاسم الكامل",
          formEmail: "البريد الإلكتروني",
          formSubject: "عنوان الرسالة / الموضوع",
          formMessage: "تفاصيل الرسالة",
          placeholderName: "أحمد محمود...",
          placeholderEmail: "ahmed@example.com",
          placeholderSubject: "فرصة عمل / استفسار عن مشروع",
          placeholderMessage: "اكتب تفاصيل المشروع أو الاستفسار هنا...",
          sendBtn: "إرسال الرسالة",
          sentBtn: "تم إرسال الرسالة بنجاح!"
        },
        stats: [
          { label: "سجلات تم تحليلها", value: "22,524", suffix: "لعبة" },
          { label: "لاعبين متزامنين (Steam CCU)", value: "5.7M+", suffix: "لاعب" },
          { label: "مبيعات التجارة الإلكترونية", value: "1.29M", suffix: "جنية" },
          { label: "وحدات إنتاجية متابعة", value: "465K+", suffix: "وحدة" }
        ],
        skills: [
          { 
            category: "أدوات تحليل البيانات والذكاء التجاري", 
            items: ["Power BI & DAX Modeling", "Power Query & ETL", "نمذجة البيانات (Data Modeling)", "Python (Pandas, NumPy)", "SQL Databases", "تصميم لوحات القيادة (Dashboards)"] 
          },
          { 
            category: "المحاسبة المالية والتكاليف الصناعية", 
            items: ["تحليل انحراف الكميات (Variance Analysis)", "توزيع وتخصيص التكاليف", "النمذجة المالية والتسعير", "إعداد الموازنات والتنبؤ", "التقارير الإدارية التنفيذية", "تقارير إكسيل البصرية و VBA"] 
          },
          { 
            category: "إدارة العمليات والتجارة الإلكترونية", 
            items: ["مؤشرات أداء التوصيل (On-Time Delivery)", "تحليل قنوات البيع", "إدارة المخزون والتخزين", "التوزيع الجغرافي للمبيعات", "تحليل معدلات الإلغاء والمرتجعات", "تحسين سلاسل التوريد"] 
          }
        ],
        projects: [
          {
            id: "steam-analytics",
            title: "دراسة وتصنيف سوق الألعاب العالمي (Steam Market Intelligence)",
            category: "تحليل البيانات الضخمة والألعاب",
            badge: "Power BI & Excel Report",
            image: steamImg,
            excelFile: "Database.xlsx",
            description: "مشروع تحليل وشامل لأكثر من 22,500 لعبة على منصة Steam، بتتبع أكثر من 5.7 مليون لاعب متزامن (CCU)، وتحليل نسب التقييمات الإيجابية والسلبية، وتوافق أنظمة التشغيل (Windows, Mac, Linux)، والنموذج المجاني مقابل المدفوع.",
            highlights: [
              "تتبع أكثر من 5,705,135 لاعب متزامن عبر قاعدة البيانات.",
              "نسبة التقييم الإيجابي العامة في المنصة 86% مقابل 14% تقييمات سلبية.",
              "تحليل هيمنة نظام Windows بنسبة 99.9% مقابل 27% لـ Mac و 18% لـ Linux.",
              "تحليل أعلى الألعاب جذباً للاعبين بقيادة Counter-Strike و PUBG و Elden Ring."
            ]
          },
          {
            id: "cost-variance",
            title: "لوحة تحليل تكاليف الإنتاج وانحراف الكميات (Manufacturing Cost Variance)",
            category: "محاسبة التكاليف والإنتاج",
            badge: "Production Order Visual Report",
            image: costImg,
            excelFile: "Production Order Visual Report.xlsx",
            description: "داشبورد احترافي مخصص لمحاسبة التكاليف الصناعية لمجموعة منتجات التجميل والعناية بالبشرة، بتتبع طاقة إنتاجية تبلغ 465,165 قطعة، وتحليل الانحراف في الكميات (3,657 قطعة) وتحديد المنتجات الأعلى مبيعاً وانحرافاً حسب شركات الإنتاج.",
            highlights: [
              "تحليل طاقة الإنتاج الإجمالية البالغة 465,165 وحدة في الفترة المحددة.",
              "كشف انحرافات الكمية البالغة 3,657 وحدة وتحديد الـ 10 منتجات المسببة للانحراف.",
              "تحديد أكثر المنتجات تحقيقاً للإيرادات بقيادة (هيرواكس أسود 1000 جم) بمبيعات 86,384 ج.م.",
              "تصنيف أوامر الإنتاج حسب الشركات المنتجة (Senor بقيادة 141 أمر إنتاجي، يليها Leven بـ 98 أمر)."
            ]
          },
          {
            id: "misuo-ecommerce",
            title: "داشبورد تحليلات مبيعات وتوصيل شركة MISUO للتجارة الإلكترونية",
            category: "تحليلات التجارة الإلكترونية وسلاسل الإمداد",
            badge: "MISUO Executive Dashboard",
            image: misuoImg,
            excelFile: "MISUO - Abdelaziz Usama Mahmoud.xlsx",
            description: "تحليل شامل لعمليات المبيعات والتوصيل لشركة MISUO بإجمالي مبيعات 1,292,886 جنيه عبر 152 طلباً، مع تتبع التوزيع الجغرافي للمحافظات، وأداء قنوات البيع، ومعدلات نجاح التوصيل والتسليم الفعلي.",
            highlights: [
              "تحليل إجمالي المبيعات البالغ 1.29 مليون جنيه متوسط قيمة الطلب 10,261 ج.م.",
              "تصدر محافظة القاهرة للطلب بـ 60 طلباً، تليها الجيزة بـ 24 طلباً ثم القليوبية بـ 11 طلباً.",
              "تفوق منصة HomeMart كأعلى قناة بيع تحقيقاً للقطع المباعة بـ 94 قطعة.",
              "تقييم كفاءة الشحن: 81% من الطلبات تم توصيلها بنجاح مقابل 18% إلغاء أو رفض."
            ]
          }
        ]
      }
    };

    function App() {
      const [lang, setLang] = useState('en');
      const [theme, setTheme] = useState(() => {
        return localStorage.getItem('portfolio_theme') || 'dark';
      });
      const [activeModal, setActiveModal] = useState(null);
      const [filterCategory, setFilterCategory] = useState('all');
      const [contactSubmitted, setContactSubmitted] = useState(false);

      // Section Form State
      const [formState, setFormState] = useState({ name: '', email: '', subject: '', message: '' });
      const [sectionContactSubmitted, setSectionContactSubmitted] = useState(false);

      // Refs for Chart instances
      const steamPieRef = useRef(null);
      const steamBarRef = useRef(null);
      const costBarRef = useRef(null);
      const costPieRef = useRef(null);
      const misuoPieRef = useRef(null);
      const misuoAreaRef = useRef(null);

      const chartInstances = useRef([]);

      // Theme Manager Effect
      useEffect(() => {
        const rootElem = document.documentElement;
        if (theme === 'dark') {
          rootElem.setAttribute('data-theme', 'dark');
          rootElem.classList.add('dark');
        } else {
          rootElem.setAttribute('data-theme', 'light');
          rootElem.classList.remove('dark');
        }
        localStorage.setItem('portfolio_theme', theme);
      }, [theme]);

      const toggleTheme = () => {
        setTheme(prev => prev === 'dark' ? 'light' : 'dark');
      };

      const toggleLang = () => {
        const nextLang = lang === 'en' ? 'ar' : 'en';
        setLang(nextLang);
        document.documentElement.lang = nextLang;
        document.documentElement.dir = nextLang === 'ar' ? 'rtl' : 'ltr';
      };

      const data = portfolioContent[lang];

      // Filtered projects
      const filteredProjects = data.projects.filter(p => {
        if (filterCategory === 'all') return true;
        if (filterCategory === 'gaming') return p.id === 'steam-analytics';
        if (filterCategory === 'cost') return p.id === 'cost-variance';
        if (filterCategory === 'ecommerce') return p.id === 'misuo-ecommerce';
        return true;
      });

      const handleSectionFormSubmit = (e) => {
        e.preventDefault();
        setSectionContactSubmitted(true);
        setTimeout(() => {
          setSectionContactSubmitted(false);
          setFormState({ name: '', email: '', subject: '', message: '' });
        }, 3000);
      };

      // Clear Chart instances before drawing new ones
      const clearCharts = () => {
        chartInstances.current.forEach(chart => {
          if (chart) chart.destroy();
        });
        chartInstances.current = [];
      };

      // Modal Chart initialization
      useEffect(() => {
        clearCharts();

        const textColor = theme === 'dark' ? '#F5F8FF' : '#14213D';
        const gridColor = theme === 'dark' ? '#233B61' : '#D8E3F5';
        const accentColor = theme === 'dark' ? '#3B82F6' : '#2563EB';

        if (activeModal === 'steam-analytics') {
          setTimeout(() => {
            if (steamPieRef.current) {
              const ctx1 = steamPieRef.current.getContext('2d');
              const c1 = new Chart(ctx1, {
                type: 'doughnut',
                data: {
                  labels: lang === 'ar' ? ['تقييم إيجابي', 'تقييم سلبي'] : ['Positive Sentiment', 'Negative Sentiment'],
                  datasets: [{
                    data: [86.0, 14.0],
                    backgroundColor: [accentColor, '#EF4444'],
                    borderWidth: 0
                  }]
                },
                options: {
                  responsive: true,
                  maintainAspectRatio: false,
                  plugins: { legend: { labels: { color: textColor, font: { size: 11 } } } }
                }
              });
              chartInstances.current.push(c1);
            }

            if (steamBarRef.current) {
              const ctx2 = steamBarRef.current.getContext('2d');
              const c2 = new Chart(ctx2, {
                type: 'bar',
                data: {
                  labels: ['CS:GO', 'PUBG', 'Dota 2', 'Apex', 'Lost Ark', 'GTA V', 'Rust', 'Elden Ring'],
                  datasets: [{
                    label: lang === 'ar' ? 'أقصى لاعبين متزامنين (CCU)' : 'Peak CCU',
                    data: [1305219, 913634, 720000, 511676, 420000, 310000, 244384, 210000],
                    backgroundColor: accentColor,
                    borderRadius: 6
                  }]
                },
                options: {
                  responsive: true,
                  maintainAspectRatio: false,
                  plugins: { legend: { display: false } },
                  scales: {
                    x: { ticks: { color: textColor, font: { size: 10 } }, grid: { color: gridColor } },
                    y: { ticks: { color: textColor, font: { size: 10 } }, grid: { color: gridColor } }
                  }
                }
              });
              chartInstances.current.push(c2);
            }
          }, 100);
        }

        if (activeModal === 'cost-variance') {
          setTimeout(() => {
            if (costBarRef.current) {
              const ctx = costBarRef.current.getContext('2d');
              const c = new Chart(ctx, {
                type: 'bar',
                data: {
                  labels: ['Black Hair Wax 1000g', 'Cold Wax 250g', 'Cold Wax 500g', 'Hard Wax Beans', 'Gold Hair Wax'],
                  datasets: [{
                    label: lang === 'ar' ? 'الإيرادات (EGP)' : 'Revenue (EGP)',
                    data: [86384, 62100, 48900, 39500, 31200],
                    backgroundColor: accentColor,
                    borderRadius: 6
                  }]
                },
                options: {
                  responsive: true,
                  maintainAspectRatio: false,
                  indexAxis: 'y',
                  plugins: { legend: { display: false } },
                  scales: {
                    x: { ticks: { color: textColor, font: { size: 10 } }, grid: { color: gridColor } },
                    y: { ticks: { color: textColor, font: { size: 10 } }, grid: { color: gridColor } }
                  }
                }
              });
              chartInstances.current.push(c);
            }

            if (costPieRef.current) {
              const ctx = costPieRef.current.getContext('2d');
              const c = new Chart(ctx, {
                type: 'doughnut',
                data: {
                  labels: ['Senor', 'Leven', 'Soft', 'Pure', 'Others'],
                  datasets: [{
                    data: [141, 98, 45, 32, 29],
                    backgroundColor: [accentColor, '#60A5FA', '#93C5FD', '#BFDBFE', '#1D4ED8'],
                    borderWidth: 0
                  }]
                },
                options: {
                  responsive: true,
                  maintainAspectRatio: false,
                  plugins: { legend: { labels: { color: textColor, font: { size: 11 } } } }
                }
              });
              chartInstances.current.push(c);
            }
          }, 100);
        }

        if (activeModal === 'misuo-ecommerce') {
          setTimeout(() => {
            if (misuoPieRef.current) {
              const ctx = misuoPieRef.current.getContext('2d');
              const c = new Chart(ctx, {
                type: 'pie',
                data: {
                  labels: lang === 'ar' ? ['تم التوصيل بنجاح', 'ملغي / ملقى'] : ['Delivered', 'Cancelled'],
                  datasets: [{
                    data: [81.5, 18.5],
                    backgroundColor: [accentColor, '#EF4444'],
                    borderWidth: 0
                  }]
                },
                options: {
                  responsive: true,
                  maintainAspectRatio: false,
                  plugins: { legend: { labels: { color: textColor, font: { size: 11 } } } }
                }
              });
              chartInstances.current.push(c);
            }

            if (misuoAreaRef.current) {
              const ctx = misuoAreaRef.current.getContext('2d');
              const c = new Chart(ctx, {
                type: 'bar',
                data: {
                  labels: ['Cairo', 'Giza', 'Qalyubia', 'Alexandria', 'Monufia', 'Sharqia'],
                  datasets: [{
                    label: lang === 'ar' ? 'عدد الطلبات' : 'Orders Count',
                    data: [60, 24, 11, 8, 6, 5],
                    backgroundColor: accentColor,
                    borderRadius: 6
                  }]
                },
                options: {
                  responsive: true,
                  maintainAspectRatio: false,
                  plugins: { legend: { display: false } },
                  scales: {
                    x: { ticks: { color: textColor, font: { size: 10 } }, grid: { color: gridColor } },
                    y: { ticks: { color: textColor, font: { size: 10 } }, grid: { color: gridColor } }
                  }
                }
              });
              chartInstances.current.push(c);
            }
          }, 100);
        }
      }, [activeModal, theme, lang]);

      return (
        <div className={`min-h-screen theme-bg-main theme-text-primary ${lang === 'ar' ? 'font-cairo' : 'font-sans'}`}>
          
          {/* Header / Navigation Bar */}
          <nav className="sticky top-0 z-40 theme-bg-nav border-b theme-border shadow-md backdrop-blur-md">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
              <div className="flex items-center justify-between h-16 sm:h-20">
                
                {/* Brand Logo */}
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-xl theme-bg-accent flex items-center justify-center font-black text-white text-lg shadow-md theme-glow">
                    AO
                  </div>
                  <div>
                    <h1 className="font-extrabold text-sm sm:text-base leading-snug theme-text-primary tracking-tight">
                      {data.personal.name}
                    </h1>
                    <p className="text-[11px] theme-text-accent font-semibold hidden sm:block">
                      {data.personal.title}
                    </p>
                  </div>
                </div>

                {/* Nav Links */}
                <div className="hidden md:flex items-center gap-6 text-xs sm:text-sm font-semibold theme-text-secondary">
                  <a href="#skills" className="hover:theme-text-accent transition-colors">
                    {lang === 'ar' ? 'المهارات' : 'Skills'}
                  </a>
                  <a href="#projects" className="hover:theme-text-accent transition-colors">
                    {lang === 'ar' ? 'المشاريع' : 'Projects'}
                  </a>
                  <a href="#contact" className="hover:theme-text-accent transition-colors">
                    {lang === 'ar' ? 'تواصل معي' : 'Contact'}
                  </a>
                </div>

                {/* Right Actions & Controls */}
                <div className="flex items-center gap-2 sm:gap-3">
                  
                  {/* Theme Switcher Button with Sun ☀️ & Moon 🌙 Icons */}
                  <button
                    onClick={toggleTheme}
                    aria-label={theme === 'dark' ? 'Switch to Light Mode' : 'Switch to Dark Mode'}
                    title={theme === 'dark' ? 'Switch to Light Mode' : 'Switch to Dark Mode'}
                    className="p-2.5 rounded-xl theme-bg-elevated border theme-border theme-text-primary theme-hover-bg transition-all flex items-center gap-1.5 text-xs font-bold shadow-sm"
                  >
                    {theme === 'dark' ? (
                      <>
                        <span className="text-amber-400 text-sm">☀️</span>
                        <span className="hidden sm:inline">Light Mode</span>
                      </>
                    ) : (
                      <>
                        <span className="text-blue-600 text-sm">🌙</span>
                        <span className="hidden sm:inline">Dark Mode</span>
                      </>
                    )}
                  </button>

                  {/* Language Toggle */}
                  <button
                    onClick={toggleLang}
                    className="px-3.5 py-2 rounded-xl theme-bg-elevated border theme-border theme-text-primary theme-hover-bg transition-all text-xs font-bold shadow-sm"
                  >
                    {lang === 'en' ? '🇪🇬 العربيّة' : '🇬🇧 English'}
                  </button>

                  {/* Download CV Button */}
                  <a
                    href={data.personal.resumePdf}
                    download={data.personal.resumePdf}
                    className="hidden md:inline-flex items-center gap-1.5 px-4 py-2 rounded-xl theme-bg-accent font-bold text-xs shadow-lg theme-glow transition-all"
                  >
                    <span>📄</span>
                    <span>{lang === 'ar' ? 'تحميل السي في (PDF)' : 'Download Resume'}</span>
                  </a>

                  {/* Scroll to Contact Section Trigger */}
                  <a
                    href="#contact"
                    className="px-4 py-2 rounded-xl theme-bg-elevated border theme-border theme-text-accent theme-hover-bg text-xs font-bold transition-all shadow-sm flex items-center gap-1.5"
                  >
                    <span>✉️</span>
                    <span>{lang === 'ar' ? 'تواصل معي' : 'Contact'}</span>
                  </a>

                </div>
              </div>
            </div>
          </nav>

          {/* Hero Section */}
          <section className="relative py-12 lg:py-20 overflow-hidden border-b theme-border theme-bg-secondary">
            {/* Subtle Electric Blue Background Glow */}
            <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-blue-500/10 rounded-full blur-3xl pointer-events-none"></div>

            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
              <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center">
                
                {/* Text Content */}
                <div className="lg:col-span-7 space-y-6">
                  
                  {/* Status Tag */}
                  <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full theme-bg-elevated border theme-border theme-text-accent text-xs font-bold shadow-sm">
                    <span className="w-2.5 h-2.5 rounded-full theme-bg-accent animate-pulse"></span>
                    <span>{lang === 'ar' ? 'متاح لمشاريع واستشارات تحليل البيانات' : 'Available for BI & Analytics Roles'}</span>
                  </div>

                  <h1 className="text-3xl sm:text-4xl lg:text-5xl font-black theme-text-primary tracking-tight leading-tight">
                    {data.personal.name}
                  </h1>

                  <h2 className="text-lg sm:text-xl font-bold theme-text-bright">
                    {data.personal.title}
                  </h2>

                  <p className="text-sm sm:text-base theme-text-secondary leading-relaxed max-w-2xl">
                    {data.personal.bio}
                  </p>

                  {/* Action Buttons */}
                  <div className="flex flex-wrap items-center gap-3 pt-2">
                    <a
                      href="#projects"
                      className="px-5 py-2.5 rounded-xl theme-bg-accent font-bold text-xs sm:text-sm shadow-lg theme-glow transition-all flex items-center gap-2"
                    >
                      <span>📊</span>
                      <span>{lang === 'ar' ? 'استكشف لوحات القيادة' : 'Explore Case Studies'}</span>
                    </a>

                    <a
                      href={data.personal.resumePdf}
                      download={data.personal.resumePdf}
                      className="px-5 py-2.5 rounded-xl theme-bg-elevated border theme-border theme-text-primary theme-hover-bg font-bold text-xs sm:text-sm shadow-sm transition-all flex items-center gap-2"
                    >
                      <span>📥</span>
                      <span>{lang === 'ar' ? 'تحميل السيرة الذاتية' : 'Download CV (PDF)'}</span>
                    </a>
                  </div>

                </div>

                {/* Profile Card & Avatar */}
                <div className="lg:col-span-5 flex justify-center">
                  <div className="relative w-full max-w-sm rounded-3xl theme-bg-card border theme-border p-6 shadow-2xl space-y-5 theme-glow">
                    <div className="relative mx-auto w-40 h-40 sm:w-48 sm:h-48 rounded-2xl overflow-hidden border-2 theme-border shadow-md">
                      <img src={profileImg} alt={data.personal.name} className="w-full h-full object-cover object-top" />
                    </div>

                    <div className="text-center space-y-1">
                      <h3 className="font-extrabold text-base theme-text-primary">{data.personal.name}</h3>
                      <p className="text-xs theme-text-secondary font-medium">{data.personal.subtitle}</p>
                      <p className="text-xs theme-text-accent font-semibold pt-1">📍 {data.personal.location}</p>
                    </div>

                    <div className="pt-2 border-t theme-border grid grid-cols-2 gap-2 text-center text-xs">
                      <div className="p-2.5 rounded-xl theme-bg-elevated border theme-border">
                        <span className="block text-[10px] theme-text-muted">Experience</span>
                        <span className="font-extrabold theme-text-primary">Senior BI / Analyst</span>
                      </div>
                      <div className="p-2.5 rounded-xl theme-bg-elevated border theme-border">
                        <span className="block text-[10px] theme-text-muted">Specialization</span>
                        <span className="font-extrabold theme-text-accent">Cost & Ops Analytics</span>
                      </div>
                    </div>
                  </div>
                </div>

              </div>
            </div>
          </section>

          {/* Key Executive Metrics Section */}
          <section className="py-12 border-b theme-border theme-bg-main">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
              <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
                {data.stats.map((stat, idx) => (
                  <div key={idx} className="p-5 rounded-2xl theme-bg-card border theme-border shadow-md text-center space-y-1 hover:border-blue-500/50 transition-all">
                    <span className="text-2xl sm:text-3xl font-black theme-text-accent block tracking-tight">
                      {stat.value}
                    </span>
                    <span className="text-xs font-bold theme-text-primary block">{stat.label}</span>
                    <span className="text-[11px] theme-text-muted block">{stat.suffix}</span>
                  </div>
                ))}
              </div>
            </div>
          </section>

          {/* Skills & Expertise Section */}
          <section id="skills" className="py-16 border-b theme-border theme-bg-secondary">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
              <div className="text-center max-w-2xl mx-auto space-y-2">
                <span className="px-3.5 py-1 rounded-full theme-bg-accent-light theme-text-accent font-bold text-xs">
                  {lang === 'ar' ? 'القدرات والمهارات الفنية' : 'Core Capabilities'}
                </span>
                <h2 className="text-2xl sm:text-3xl font-black theme-text-primary">
                  {lang === 'ar' ? 'الخبرات والأدوات التخصصية' : 'Technical & Domain Expertise'}
                </h2>
                <p className="text-xs sm:text-sm theme-text-secondary">
                  {lang === 'ar' 
                    ? 'دمج متقدم بين تحليلات البيانات الضخمة، التكاليف الصناعية، وإدارة سلاسل التوريد.'
                    : 'Integrating big data analytics, manufacturing cost accounting, and supply chain logistics.'}
                </p>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                {data.skills.map((skillGroup, idx) => (
                  <div key={idx} className="p-6 rounded-2xl theme-bg-card border theme-border shadow-md space-y-4 hover:border-blue-500/40 transition-all">
                    <h3 className="font-extrabold text-sm sm:text-base theme-text-bright border-b theme-border pb-3">
                      {skillGroup.category}
                    </h3>
                    <ul className="space-y-2.5">
                      {skillGroup.items.map((item, itemIdx) => (
                        <li key={itemIdx} className="flex items-center gap-2.5 text-xs theme-text-primary font-medium">
                          <span className="w-1.5 h-1.5 rounded-full theme-bg-accent"></span>
                          <span>{item}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                ))}
              </div>
            </div>
          </section>

          {/* Projects & Case Studies */}
          <section id="projects" className="py-16 border-b theme-border theme-bg-main">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
              
              <div className="flex flex-col md:flex-row md:items-end justify-between gap-6">
                <div>
                  <span className="px-3.5 py-1 rounded-full theme-bg-accent-light theme-text-accent font-bold text-xs">
                    {lang === 'ar' ? 'المشاريع التطبيقية' : 'Portfolio Showcase'}
                  </span>
                  <h2 className="text-2xl sm:text-3xl font-black theme-text-primary mt-2">
                    {lang === 'ar' ? 'معرض لوحات القيادة والتطبيقات المباشرة' : 'Executive Dashboards & Case Studies'}
                  </h2>
                </div>

                {/* Project Category Filter */}
                <div className="flex flex-wrap gap-2 p-1.5 rounded-2xl theme-bg-elevated border theme-border">
                  <button
                    onClick={() => setFilterCategory('all')}
                    className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all ${
                      filterCategory === 'all'
                        ? 'theme-bg-accent shadow-md'
                        : 'theme-text-secondary hover:theme-text-primary'
                    }`}
                  >
                    {lang === 'ar' ? 'الكل' : 'All Projects'}
                  </button>
                  <button
                    onClick={() => setFilterCategory('gaming')}
                    className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all ${
                      filterCategory === 'gaming'
                        ? 'theme-bg-accent shadow-md'
                        : 'theme-text-secondary hover:theme-text-primary'
                    }`}
                  >
                    {lang === 'ar' ? 'الألعاب والبيانات' : 'Gaming & Market'}
                  </button>
                  <button
                    onClick={() => setFilterCategory('cost')}
                    className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all ${
                      filterCategory === 'cost'
                        ? 'theme-bg-accent shadow-md'
                        : 'theme-text-secondary hover:theme-text-primary'
                    }`}
                  >
                    {lang === 'ar' ? 'التكاليف والإنتاج' : 'Cost & Production'}
                  </button>
                  <button
                    onClick={() => setFilterCategory('ecommerce')}
                    className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all ${
                      filterCategory === 'ecommerce'
                        ? 'theme-bg-accent shadow-md'
                        : 'theme-text-secondary hover:theme-text-primary'
                    }`}
                  >
                    {lang === 'ar' ? 'التجارة الإلكترونية' : 'E-Commerce BI'}
                  </button>
                </div>
              </div>

              {/* Projects Grid */}
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                {filteredProjects.map((project) => (
                  <div key={project.id} className="group rounded-3xl theme-bg-card border theme-border overflow-hidden shadow-xl hover:shadow-2xl hover:border-blue-500/50 transition-all duration-300 flex flex-col justify-between">
                    
                    <div>
                      {/* Image Preview */}
                      <div className="relative h-48 sm:h-52 overflow-hidden theme-bg-elevated border-b theme-border">
                        <img
                          src={project.image}
                          alt={project.title}
                          className="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500"
                        />
                        <span className="absolute top-3 right-3 px-3 py-1 rounded-full theme-bg-card border theme-border theme-text-accent text-[11px] font-bold shadow-md">
                          {project.badge}
                        </span>
                      </div>

                      {/* Content */}
                      <div className="p-6 space-y-4">
                        <span className="text-[11px] font-extrabold theme-text-bright uppercase tracking-wider block">
                          {project.category}
                        </span>
                        <h3 className="font-extrabold text-base theme-text-primary leading-snug">
                          {project.title}
                        </h3>
                        <p className="text-xs theme-text-secondary leading-relaxed line-clamp-3">
                          {project.description}
                        </p>

                        <div className="space-y-2 pt-2 border-t theme-border">
                          <span className="text-[11px] font-bold theme-text-primary block">Key Insights:</span>
                          <ul className="space-y-1">
                            {project.highlights.slice(0, 2).map((h, hIdx) => (
                              <li key={hIdx} className="text-[11px] theme-text-secondary flex items-start gap-1.5">
                                <span className="theme-text-accent font-bold">✓</span>
                                <span>{h}</span>
                              </li>
                            ))}
                          </ul>
                        </div>
                      </div>
                    </div>

                    {/* Footer Actions */}
                    <div className="p-6 pt-0 space-y-2">
                      <button
                        onClick={() => setActiveModal(project.id)}
                        className="w-full py-2.5 rounded-xl theme-bg-accent font-bold text-xs shadow-md transition-all flex items-center justify-center gap-2"
                      >
                        <span>📈</span>
                        <span>{lang === 'ar' ? 'عرض الداشبورد التفاعلي' : 'View Interactive Dashboard'}</span>
                      </button>

                      <a
                        href={project.excelFile}
                        download={project.excelFile}
                        className="w-full py-2 rounded-xl theme-bg-elevated border theme-border theme-text-primary theme-hover-bg font-semibold text-xs transition-all flex items-center justify-center gap-1.5"
                      >
                        <span>📊</span>
                        <span>{lang === 'ar' ? 'تحميل تقرير إكسيل المصدري' : 'Download Dataset (Excel)'}</span>
                      </a>
                    </div>

                  </div>
                ))}
              </div>

            </div>
          </section>

          {/* ================= DEDICATED CONTACT SECTION (Matching Reference Design) ================= */}
          <section id="contact" className="py-20 border-b theme-border theme-bg-secondary relative overflow-hidden">
            {/* Subtle Blue Glow in background */}
            <div className="absolute top-1/2 right-10 -translate-y-1/2 w-80 h-80 bg-blue-500/10 rounded-full blur-3xl pointer-events-none"></div>

            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
              <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-12 items-start">
                
                {/* Left Column: Contact Info & Cards Stack */}
                <div className="lg:col-span-5 space-y-6">
                  <div>
                    <h2 className="text-3xl font-black theme-text-primary tracking-tight mb-3">
                      {data.contactSection.title}
                    </h2>
                    <p className="text-xs sm:text-sm theme-text-secondary leading-relaxed">
                      {data.contactSection.subtitle}
                    </p>
                  </div>

                  {/* Vertical Stack of Sleek Contact Cards */}
                  <div className="space-y-4 pt-2">
                    
                    {/* Card 1: Email */}
                    <div className="p-4 rounded-2xl theme-bg-card border theme-border shadow-md flex items-center gap-4 hover:border-blue-500/50 transition-all">
                      <div className="w-12 h-12 rounded-xl theme-bg-accent/15 border theme-border flex items-center justify-center text-xl text-blue-500">
                        ✉️
                      </div>
                      <div className="space-y-0.5 overflow-hidden">
                        <span className="text-[10px] font-extrabold theme-text-muted uppercase tracking-wider block">EMAIL</span>
                        <a href={`mailto:${data.personal.email}`} className="text-xs sm:text-sm font-bold theme-text-primary hover:theme-text-accent transition-colors block truncate">
                          {data.personal.email}
                        </a>
                      </div>
                    </div>

                    {/* Card 2: Phone */}
                    <div className="p-4 rounded-2xl theme-bg-card border theme-border shadow-md flex items-center gap-4 hover:border-blue-500/50 transition-all">
                      <div className="w-12 h-12 rounded-xl theme-bg-accent/15 border theme-border flex items-center justify-center text-xl text-blue-500">
                        📞
                      </div>
                      <div className="space-y-0.5">
                        <span className="text-[10px] font-extrabold theme-text-muted uppercase tracking-wider block">PHONE</span>
                        <a href={`tel:${data.personal.phone}`} className="text-xs sm:text-sm font-bold theme-text-primary hover:theme-text-accent transition-colors block">
                          {data.personal.phone}
                        </a>
                      </div>
                    </div>

                    {/* Card 3: LinkedIn */}
                    <div className="p-4 rounded-2xl theme-bg-card border theme-border shadow-md flex items-center gap-4 hover:border-blue-500/50 transition-all">
                      <div className="w-12 h-12 rounded-xl theme-bg-accent/15 border theme-border flex items-center justify-center text-xl text-blue-500 font-bold">
                        in
                      </div>
                      <div className="space-y-0.5 overflow-hidden">
                        <span className="text-[10px] font-extrabold theme-text-muted uppercase tracking-wider block">LINKEDIN</span>
                        <a href={data.personal.linkedin} target="_blank" rel="noopener noreferrer" className="text-xs sm:text-sm font-bold theme-text-primary hover:theme-text-accent transition-colors block truncate">
                          {data.personal.linkedinDisplay}
                        </a>
                      </div>
                    </div>

                    {/* Card 4: Location */}
                    <div className="p-4 rounded-2xl theme-bg-card border theme-border shadow-md flex items-center gap-4 hover:border-blue-500/50 transition-all">
                      <div className="w-12 h-12 rounded-xl theme-bg-accent/15 border theme-border flex items-center justify-center text-xl text-blue-500">
                        📍
                      </div>
                      <div className="space-y-0.5">
                        <span className="text-[10px] font-extrabold theme-text-muted uppercase tracking-wider block">LOCATION</span>
                        <span className="text-xs sm:text-sm font-bold theme-text-primary block">
                          {data.personal.location}
                        </span>
                      </div>
                    </div>

                  </div>
                </div>

                {/* Right Column: Contact Form Box */}
                <div className="lg:col-span-7">
                  <div className="p-6 sm:p-8 rounded-3xl theme-bg-card border theme-border shadow-2xl space-y-6 theme-glow">
                    <form onSubmit={handleSectionFormSubmit} className="space-y-5">
                      
                      {/* Name Field */}
                      <div className="space-y-2">
                        <label className="text-xs font-bold theme-text-primary block">
                          {data.contactSection.formName}
                        </label>
                        <input
                          type="text"
                          required
                          value={formState.name}
                          onChange={(e) => setFormState({ ...formState, name: e.target.value })}
                          placeholder={data.contactSection.placeholderName}
                          className="w-full px-4 py-3 rounded-xl theme-bg-elevated border theme-border text-xs sm:text-sm theme-text-primary focus:outline-none focus:border-blue-500 transition-colors"
                        />
                      </div>

                      {/* Email Field */}
                      <div className="space-y-2">
                        <label className="text-xs font-bold theme-text-primary block">
                          {data.contactSection.formEmail}
                        </label>
                        <input
                          type="email"
                          required
                          value={formState.email}
                          onChange={(e) => setFormState({ ...formState, email: e.target.value })}
                          placeholder={data.contactSection.placeholderEmail}
                          className="w-full px-4 py-3 rounded-xl theme-bg-elevated border theme-border text-xs sm:text-sm theme-text-primary focus:outline-none focus:border-blue-500 transition-colors"
                        />
                      </div>

                      {/* Subject Field */}
                      <div className="space-y-2">
                        <label className="text-xs font-bold theme-text-primary block">
                          {data.contactSection.formSubject}
                        </label>
                        <input
                          type="text"
                          required
                          value={formState.subject}
                          onChange={(e) => setFormState({ ...formState, subject: e.target.value })}
                          placeholder={data.contactSection.placeholderSubject}
                          className="w-full px-4 py-3 rounded-xl theme-bg-elevated border theme-border text-xs sm:text-sm theme-text-primary focus:outline-none focus:border-blue-500 transition-colors"
                        />
                      </div>

                      {/* Message Field */}
                      <div className="space-y-2">
                        <label className="text-xs font-bold theme-text-primary block">
                          {data.contactSection.formMessage}
                        </label>
                        <textarea
                          rows={4}
                          required
                          value={formState.message}
                          onChange={(e) => setFormState({ ...formState, message: e.target.value })}
                          placeholder={data.contactSection.placeholderMessage}
                          className="w-full px-4 py-3 rounded-xl theme-bg-elevated border theme-border text-xs sm:text-sm theme-text-primary focus:outline-none focus:border-blue-500 transition-colors resize-none"
                        ></textarea>
                      </div>

                      {/* Submit Button */}
                      <button
                        type="submit"
                        className="w-full py-3.5 rounded-xl theme-bg-accent text-white font-extrabold text-xs sm:text-sm shadow-lg theme-glow transition-all flex items-center justify-center gap-2 hover:opacity-95"
                      >
                        <span>✈️</span>
                        <span>
                          {sectionContactSubmitted ? data.contactSection.sentBtn : data.contactSection.sendBtn}
                        </span>
                      </button>

                    </form>
                  </div>
                </div>

              </div>
            </div>
          </section>

          {/* Footer */}
          <footer className="py-10 theme-bg-card border-t theme-border text-center space-y-4">
            <div className="max-w-7xl mx-auto px-4 space-y-2">
              <h3 className="font-extrabold text-sm theme-text-primary">{data.personal.name}</h3>
              <p className="text-xs theme-text-secondary">{data.personal.title}</p>
              <p className="text-[11px] theme-text-muted pt-2">
                © 2026 {data.personal.name}. All Rights Reserved. Designed with Modern Electric Blue & Navy Architecture.
              </p>
            </div>
          </footer>

          {/* ================= MODALS ================= */}

          {/* Modal 1: Steam Gaming Analytics */}
          {activeModal === 'steam-analytics' && (
            <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-md overflow-y-auto">
              <div className="relative w-full max-w-4xl theme-bg-card border theme-border rounded-3xl p-6 space-y-6 shadow-2xl my-8">
                <div className="flex justify-between items-center border-b theme-border pb-4">
                  <div>
                    <span className="text-xs font-bold theme-text-accent">Steam Gaming Intelligence</span>
                    <h3 className="text-lg font-extrabold theme-text-primary">
                      {lang === 'ar' ? 'تحليل سوق الألعاب العالمي على منصة Steam' : 'Steam Gaming Market Analytics'}
                    </h3>
                  </div>
                  <button onClick={() => setActiveModal(null)} className="w-8 h-8 rounded-full theme-bg-elevated border theme-border theme-text-secondary hover:theme-text-primary font-bold">✕</button>
                </div>

                {/* Dashboard Grid */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div className="p-4 rounded-2xl theme-bg-elevated border theme-border space-y-2">
                    <h4 className="text-xs font-bold theme-text-accent">Positive vs Negative Sentiment Ratio</h4>
                    <div className="h-48"><canvas ref={steamPieRef}></canvas></div>
                  </div>

                  <div className="p-4 rounded-2xl theme-bg-elevated border theme-border space-y-2">
                    <h4 className="text-xs font-bold theme-text-accent">Top Games by Concurrent Players (CCU)</h4>
                    <div className="h-48"><canvas ref={steamBarRef}></canvas></div>
                  </div>
                </div>

                {/* Excel Download Banner */}
                <div className="p-4 rounded-2xl theme-bg-elevated border theme-border flex flex-col sm:flex-row items-center justify-between gap-4">
                  <div>
                    <h4 className="text-xs font-bold theme-text-primary">Full Raw Market Dataset</h4>
                    <p className="text-[11px] theme-text-secondary">22,524 titles indexed with full pricing and OS breakdown.</p>
                  </div>
                  <a href="Database.xlsx" download="Database.xlsx" className="px-4 py-2 rounded-xl theme-bg-accent text-xs font-bold transition-all">
                    📥 Download Database.xlsx
                  </a>
                </div>
              </div>
            </div>
          )}

          {/* Modal 2: Cost Accounting Variance */}
          {activeModal === 'cost-variance' && (
            <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-md overflow-y-auto">
              <div className="relative w-full max-w-4xl theme-bg-card border theme-border rounded-3xl p-6 space-y-6 shadow-2xl my-8">
                <div className="flex justify-between items-center border-b theme-border pb-4">
                  <div>
                    <span className="text-xs font-bold theme-text-accent">Manufacturing Cost BI</span>
                    <h3 className="text-lg font-extrabold theme-text-primary">
                      {lang === 'ar' ? 'داشبورد انحراف الكميات والتكاليف الصناعية' : 'Manufacturing Quantity Variance Dashboard'}
                    </h3>
                  </div>
                  <button onClick={() => setActiveModal(null)} className="w-8 h-8 rounded-full theme-bg-elevated border theme-border theme-text-secondary hover:theme-text-primary font-bold">✕</button>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div className="p-4 rounded-2xl theme-bg-elevated border theme-border space-y-2">
                    <h4 className="text-xs font-bold theme-text-accent">Top Revenue SKUs (EGP)</h4>
                    <div className="h-48"><canvas ref={costBarRef}></canvas></div>
                  </div>

                  <div className="p-4 rounded-2xl theme-bg-elevated border theme-border space-y-2">
                    <h4 className="text-xs font-bold theme-text-accent">Production Orders Distribution by Brand</h4>
                    <div className="h-48"><canvas ref={costPieRef}></canvas></div>
                  </div>
                </div>

                <div className="p-4 rounded-2xl theme-bg-elevated border theme-border flex flex-col sm:flex-row items-center justify-between gap-4">
                  <div>
                    <h4 className="text-xs font-bold theme-text-primary">Production Visual Report Excel Source</h4>
                    <p className="text-[11px] theme-text-secondary">Detailed work order breakdown across 465,165 units.</p>
                  </div>
                  <a href="Production Order Visual Report.xlsx" download="Production Order Visual Report.xlsx" className="px-4 py-2 rounded-xl theme-bg-accent text-xs font-bold transition-all">
                    📥 Download Production Order Report.xlsx
                  </a>
                </div>
              </div>
            </div>
          )}

          {/* Modal 3: MISUO E-Commerce */}
          {activeModal === 'misuo-ecommerce' && (
            <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-md overflow-y-auto">
              <div className="relative w-full max-w-4xl theme-bg-card border theme-border rounded-3xl p-6 space-y-6 shadow-2xl my-8">
                <div className="flex justify-between items-center border-b theme-border pb-4">
                  <div>
                    <span className="text-xs font-bold theme-text-accent">E-Commerce Supply Chain BI</span>
                    <h3 className="text-lg font-extrabold theme-text-primary">
                      {lang === 'ar' ? 'داشبورد مبيعات وشحن شركة MISUO' : 'MISUO Sales & SLA Fulfillment Analytics'}
                    </h3>
                  </div>
                  <button onClick={() => setActiveModal(null)} className="w-8 h-8 rounded-full theme-bg-elevated border theme-border theme-text-secondary hover:theme-text-primary font-bold">✕</button>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div className="p-4 rounded-2xl theme-bg-elevated border theme-border space-y-2">
                    <h4 className="text-xs font-bold theme-text-accent">Delivery SLA Success Rate</h4>
                    <div className="h-48"><canvas ref={misuoPieRef}></canvas></div>
                  </div>

                  <div className="p-4 rounded-2xl theme-bg-elevated border theme-border space-y-2">
                    <h4 className="text-xs font-bold theme-text-accent">Governorate Demand Breakdown</h4>
                    <div className="h-48"><canvas ref={misuoAreaRef}></canvas></div>
                  </div>
                </div>

                <div className="p-4 rounded-2xl theme-bg-elevated border theme-border flex flex-col sm:flex-row items-center justify-between gap-4">
                  <div>
                    <h4 className="text-xs font-bold theme-text-primary">MISUO Master Sales File</h4>
                    <p className="text-[11px] theme-text-secondary">Complete order history and shipping SLA performance metrics.</p>
                  </div>
                  <a href="MISUO - Abdelaziz Usama Mahmoud.xlsx" download="MISUO - Abdelaziz Usama Mahmoud.xlsx" className="px-4 py-2 rounded-xl theme-bg-accent text-xs font-bold transition-all">
                    📥 Download MISUO Excel File.xlsx
                  </a>
                </div>
              </div>
            </div>
          )}

        </div>
      );
    }

    ReactDOM.createRoot(document.getElementById('root')).render(<App />);
  </script>
</body>
</html>"""

html_content = template.replace('__PROFILE_B64__', profile_b64)
html_content = html_content.replace('__STEAM_B64__', steam_b64)
html_content = html_content.replace('__COST_B64__', cost_b64)
html_content = html_content.replace('__MISUO_B64__', misuo_b64)

html_content = html_content.replace('__STEAM_DATA__', json.dumps(steam_data, ensure_ascii=False))
html_content = html_content.replace('__COST_DATA__', json.dumps(cost_data, ensure_ascii=False))
html_content = html_content.replace('__MISUO_DATA__', json.dumps(misuo_data, ensure_ascii=False))

# Save to Downloads
premium_downloads_path = os.path.join(downloads_path, 'portfolio_abdelaziz_premium.html')
with open(premium_downloads_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

# Save to Scratch
premium_scratch_path = os.path.join(r'C:\Users\Enter Computer\.gemini\antigravity\scratch', 'portfolio_abdelaziz_premium.html')
with open(premium_scratch_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Successfully added Dedicated Contact Section matching reference image to portfolio_abdelaziz_premium.html!')
