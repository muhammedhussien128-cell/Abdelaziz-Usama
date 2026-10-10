import json
import base64
import os

scratch = r'C:\Users\Enter Computer\.gemini\antigravity\scratch\abdelaziz-portfolio'
downloads = r'C:\Users\Enter Computer\Downloads'

def get_base64(path):
    with open(path, 'rb') as f:
        return 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('utf-8')

profile_b64 = get_base64(os.path.join(scratch, 'public', 'assets', 'profile.jpg'))
steam_b64 = get_base64(os.path.join(scratch, 'public', 'assets', 'dashboard_steam.jpg'))
cost_b64 = get_base64(os.path.join(scratch, 'public', 'assets', 'dashboard_cost.jpg'))
misuo_b64 = get_base64(os.path.join(scratch, 'public', 'assets', 'dashboard_misuo.jpg'))

with open(os.path.join(scratch, 'src', 'data', 'steam_data.json'), 'r', encoding='utf-8') as f:
    steam_data = json.load(f)

with open(os.path.join(scratch, 'src', 'data', 'cost_data.json'), 'r', encoding='utf-8') as f:
    cost_data = json.load(f)

with open(os.path.join(scratch, 'src', 'data', 'misuo_data.json'), 'r', encoding='utf-8') as f:
    misuo_data = json.load(f)

template = '''<!DOCTYPE html>
<html lang="ar" dir="rtl" class="dark scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>عبدالعزيز أسامة محمود | معرض أعمال تحليل البيانات والذكاء التجاري</title>

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
          colors: {
            bgMain: '#111315',
            bgCard: '#191C1F',
            bgElevated: '#202428',
            borderMuted: '#30363B',
            textPrimary: '#F1F3F4',
            textSecondary: '#A3ADB5',
            accentPrimary: '#78A99B',
            accentHover: '#8DBBAC',
            bgHover: '#252A2D'
          },
          fontFamily: {
            cairo: ['Cairo', 'sans-serif'],
            sans: ['Plus Jakarta Sans', 'Cairo', 'sans-serif']
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
    body { background-color: #111315; color: #F1F3F4; font-family: 'Cairo', sans-serif; }

    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #111315; }
    ::-webkit-scrollbar-thumb { background: #30363B; border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: #78A99B; }
  </style>
</head>
<body class="bg-[#111315]">
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

    function App() {
      const [lang, setLang] = useState('ar');
      const [activeModal, setActiveModal] = useState(null);
      const [searchTerm, setSearchTerm] = useState('');
      const [freeFilter, setFreeFilter] = useState('all');
      const [contactSubmitted, setContactSubmitted] = useState(false);

      const steamCcURef = useRef(null);
      const steamSentimentRef = useRef(null);
      const costVarianceRef = useRef(null);
      const costSalesRef = useRef(null);
      const misuoDeliveryRef = useRef(null);
      const misuoAreaRef = useRef(null);

      const chartInstances = useRef({});

      const destroyChart = (id) => {
        if (chartInstances.current[id]) {
          chartInstances.current[id].destroy();
          delete chartInstances.current[id];
        }
      };

      useEffect(() => {
        if (activeModal === 'steam-analytics') {
          setTimeout(() => {
            if (steamCcURef.current) {
              destroyChart('steamCcu');
              chartInstances.current['steamCcu'] = new Chart(steamCcURef.current, {
                type: 'bar',
                data: {
                  labels: steamData.top_ccu.map(g => g.name.length > 18 ? g.name.substring(0, 18) + '...' : g.name),
                  datasets: [{
                    label: lang === 'ar' ? 'اللاعبين المتزامنين' : 'CCU',
                    data: steamData.top_ccu.map(g => g.ccu),
                    backgroundColor: '#78A99B',
                    borderRadius: 6
                  }]
                },
                options: {
                  responsive: true,
                  maintainAspectRatio: false,
                  plugins: { legend: { display: false } },
                  scales: {
                    x: { ticks: { color: '#A3ADB5' }, grid: { color: '#30363B' } },
                    y: { ticks: { color: '#A3ADB5' }, grid: { color: '#30363B' } }
                  }
                }
              });
            }

            if (steamSentimentRef.current) {
              destroyChart('steamSentiment');
              chartInstances.current['steamSentiment'] = new Chart(steamSentimentRef.current, {
                type: 'doughnut',
                data: {
                  labels: [lang === 'ar' ? 'تقييمات إيجابية (86%)' : 'Positive', lang === 'ar' ? 'تقييمات سلبية (14%)' : 'Negative'],
                  datasets: [{
                    data: [steamData.total_positive, steamData.total_negative],
                    backgroundColor: ['#81C784', '#E57373']
                  }]
                },
                options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'bottom', labels: { color: '#A3ADB5' } } } }
              });
            }
          }, 100);
        }

        if (activeModal === 'cost-variance') {
          setTimeout(() => {
            if (costVarianceRef.current) {
              destroyChart('costVariance');
              chartInstances.current['costVariance'] = new Chart(costVarianceRef.current, {
                type: 'bar',
                data: {
                  labels: costData.top_variance_products.map(p => p.name.length > 22 ? p.name.substring(0, 22) + '...' : p.name),
                  datasets: [{
                    label: lang === 'ar' ? 'انحراف الكمية' : 'Variance',
                    data: costData.top_variance_products.map(p => p.variance),
                    backgroundColor: '#E57373',
                    borderRadius: 6
                  }]
                },
                options: {
                  indexAxis: 'y',
                  responsive: true,
                  maintainAspectRatio: false,
                  plugins: { legend: { display: false } },
                  scales: {
                    x: { ticks: { color: '#A3ADB5' }, grid: { color: '#30363B' } },
                    y: { ticks: { color: '#A3ADB5' }, grid: { color: '#30363B' } }
                  }
                }
              });
            }

            if (costSalesRef.current) {
              destroyChart('costSales');
              chartInstances.current['costSales'] = new Chart(costSalesRef.current, {
                type: 'bar',
                data: {
                  labels: costData.top_sales_products.map(p => p.name.length > 22 ? p.name.substring(0, 22) + '...' : p.name),
                  datasets: [{
                    label: lang === 'ar' ? 'المبيعات (جنية)' : 'Sales (EGP)',
                    data: costData.top_sales_products.map(p => p.sales),
                    backgroundColor: '#81C784',
                    borderRadius: 6
                  }]
                },
                options: {
                  indexAxis: 'y',
                  responsive: true,
                  maintainAspectRatio: false,
                  plugins: { legend: { display: false } },
                  scales: {
                    x: { ticks: { color: '#A3ADB5' }, grid: { color: '#30363B' } },
                    y: { ticks: { color: '#A3ADB5' }, grid: { color: '#30363B' } }
                  }
                }
              });
            }
          }, 100);
        }

        if (activeModal === 'misuo-ecommerce') {
          setTimeout(() => {
            if (misuoDeliveryRef.current) {
              destroyChart('misuoDelivery');
              chartInstances.current['misuoDelivery'] = new Chart(misuoDeliveryRef.current, {
                type: 'doughnut',
                data: {
                  labels: misuoData.delivery_breakdown.map(d => d.status + ' (' + d.percentage + '%)'),
                  datasets: [{
                    data: misuoData.delivery_breakdown.map(d => d.percentage),
                    backgroundColor: ['#81C784', '#FFB74D', '#E57373']
                  }]
                },
                options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'bottom', labels: { color: '#A3ADB5' } } } }
              });
            }

            if (misuoAreaRef.current) {
              destroyChart('misuoArea');
              chartInstances.current['misuoArea'] = new Chart(misuoAreaRef.current, {
                type: 'bar',
                data: {
                  labels: misuoData.orders_by_area.map(a => a.city),
                  datasets: [{
                    label: lang === 'ar' ? 'عدد الطلبات' : 'Orders',
                    data: misuoData.orders_by_area.map(a => a.orders),
                    backgroundColor: '#78A99B',
                    borderRadius: 6
                  }]
                },
                options: {
                  responsive: true,
                  maintainAspectRatio: false,
                  plugins: { legend: { display: false } },
                  scales: {
                    x: { ticks: { color: '#A3ADB5' }, grid: { color: '#30363B' } },
                    y: { ticks: { color: '#A3ADB5' }, grid: { color: '#30363B' } }
                  }
                }
              });
            }
          }, 100);
        }
      }, [activeModal, lang]);

      const filteredGames = steamData.sample_games.filter(g => {
        const matchesSearch = g.name.toLowerCase().includes(searchTerm.toLowerCase()) || g.developer.toLowerCase().includes(searchTerm.toLowerCase());
        if (freeFilter === 'free') return matchesSearch && g.is_free;
        if (freeFilter === 'paid') return matchesSearch && !g.is_free;
        return matchesSearch;
      });

      return (
        <div className="min-h-screen bg-[#111315] text-[#F1F3F4]">
          
          {/* Header */}
          <nav className="sticky top-0 z-40 bg-[#111315]/95 border-b border-[#30363B] px-6 py-3.5 flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-9 h-9 rounded-xl bg-[#202428] border border-[#30363B] flex items-center justify-center font-bold text-[#78A99B]">
                📊
              </div>
              <div>
                <span className="text-base font-bold text-[#F1F3F4] block">{lang === 'ar' ? 'عبدالعزيز أسامة محمود' : 'Abdelaziz Osama Mahmoud'}</span>
                <span className="text-[11px] text-[#78A99B] font-semibold">{lang === 'ar' ? 'محلل بيانات أول & BI | محاسب تكاليف' : 'Senior Data Analyst & Cost Accountant'}</span>
              </div>
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={() => setLang(lang === 'ar' ? 'en' : 'ar')}
                className="px-3 py-1.5 rounded-lg bg-[#191C1F] border border-[#30363B] text-xs font-semibold text-[#F1F3F4] hover:bg-[#252A2D]"
              >
                🌐 {lang === 'ar' ? 'English' : 'العربية'}
              </button>
              <a
                href="Abdelaziz Usama Mahmoud Abdelaziz Resume.pdf"
                download="Abdelaziz Usama Mahmoud Abdelaziz Resume.pdf"
                target="_blank"
                className="px-3 py-1.5 rounded-xl bg-[#202428] border border-[#30363B] text-[#78A99B] font-bold text-xs shadow-sm hover:bg-[#252A2D] flex items-center gap-1"
              >
                📥 {lang === 'ar' ? 'الـ CV (PDF)' : 'CV (PDF)'}
              </a>
              <button
                onClick={() => setActiveModal('contact')}
                className="px-3.5 py-1.5 rounded-xl bg-[#78A99B] hover:bg-[#8DBBAC] text-[#111315] font-bold text-xs shadow-sm"
              >
                ✉️ {lang === 'ar' ? 'تواصل' : 'Contact'}
              </button>
            </div>
          </nav>

          {/* Hero Section */}
          <section className="py-12 px-6 max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-8 items-center bg-[#111315]">
            <div className="lg:col-span-8 text-right">
              <span className="px-3 py-1 rounded-full bg-[#191C1F] border border-[#30363B] text-[#78A99B] text-xs font-semibold mb-3 inline-block">
                🟢 {lang === 'ar' ? 'خبير تحليل البيانات والذكاء التجاري ومحاسبة التكاليف' : 'Data Analytics & Cost Accounting Expert'}
              </span>
              <h1 className="text-3xl sm:text-4xl font-extrabold mb-3 leading-tight text-[#F1F3F4]">
                {lang === 'ar' ? 'عبدالعزيز أسامة محمود' : 'Abdelaziz Osama Mahmoud'}
              </h1>
              <p className="text-xl font-bold text-[#78A99B] mb-4">
                {lang === 'ar' ? 'محلل بيانات أول ومختص الذكاء التجاري (BI Specialist) | محاسب تكاليف' : 'Senior Data Analyst & BI Specialist | Cost Accountant'}
              </p>
              <p className="text-[#A3ADB5] text-xs sm:text-sm leading-relaxed mb-6 max-w-2xl">
                {lang === 'ar'
                  ? 'محلل بيانات محترف ذو خبرة متقدمة في ربط التحليل المالي وتحليل التكاليف بذكاء الأعمال (Business Intelligence). متمكن في تصميم وتطوير لوحات القيادة التفاعلية (Dashboards) لتتبع الأداء المالي والإنتاجي، وتحليل سلوك المستهلك وتوصيل المبيعات.'
                  : 'Professional Data Analyst with advanced background in merging Cost Accounting and Financial Analysis with modern Business Intelligence.'}
              </p>

              <div className="flex flex-wrap gap-3">
                <a href="#projects" className="px-5 py-2.5 rounded-xl bg-[#78A99B] hover:bg-[#8DBBAC] text-[#111315] font-bold text-xs shadow-sm">
                  🚀 {lang === 'ar' ? 'استكشف لوحات القيادة التفاعلية' : 'Explore Interactive Dashboards'}
                </a>
                <a href="Abdelaziz Usama Mahmoud Abdelaziz Resume.pdf" download="Abdelaziz Usama Mahmoud Abdelaziz Resume.pdf" target="_blank" className="px-5 py-2.5 rounded-xl bg-[#202428] border border-[#30363B] text-[#F1F3F4] font-bold text-xs shadow-sm flex items-center gap-1.5 hover:bg-[#252A2D]">
                  📥 {lang === 'ar' ? 'تحميل السيرة الذاتية (PDF CV)' : 'Download CV (PDF)'}
                </a>
                <button onClick={() => setActiveModal('contact')} className="px-5 py-2.5 rounded-xl bg-[#191C1F] border border-[#30363B] text-[#A3ADB5] hover:text-[#F1F3F4] text-xs font-semibold">
                  📩 {lang === 'ar' ? 'تواصل معي مباشرة' : 'Get In Touch'}
                </button>
              </div>
            </div>

            {/* Profile Image */}
            <div className="lg:col-span-4 flex justify-center">
              <div className="relative w-52 sm:w-60 rounded-2xl bg-[#191C1F] p-2 border border-[#30363B] shadow-lg">
                <img src={profileImg} alt="Profile" className="w-full h-[260px] object-cover rounded-xl" />
                <div className="mt-2 p-2 rounded-lg bg-[#202428] text-center border border-[#30363B]">
                  <p className="text-[10px] text-[#78A99B] font-bold uppercase">{lang === 'ar' ? 'محاسب تكاليف & محلل بيانات' : 'Cost Accountant & Data Analyst'}</p>
                  <p className="text-xs font-bold text-[#F1F3F4]">عبدالعزيز اسامه محمود</p>
                </div>
              </div>
            </div>
          </section>

          {/* Impact Numbers */}
          <section className="py-8 bg-[#111315] border-y border-[#30363B]">
            <div className="max-w-7xl mx-auto px-6 grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
              <div className="p-4 rounded-xl bg-[#191C1F] border border-[#30363B]">
                <p className="text-2xl sm:text-3xl font-black text-[#F1F3F4]">22,524</p>
                <p className="text-[11px] text-[#A3ADB5] mt-0.5">{lang === 'ar' ? 'سجل لعبة تم تحليله' : 'Games Analyzed'}</p>
              </div>
              <div className="p-4 rounded-xl bg-[#191C1F] border border-[#30363B]">
                <p className="text-2xl sm:text-3xl font-black text-[#78A99B]">5.7M+</p>
                <p className="text-[11px] text-[#A3ADB5] mt-0.5">{lang === 'ar' ? 'لاعبين متزامنين Steam' : 'Steam CCU Players'}</p>
              </div>
              <div className="p-4 rounded-xl bg-[#191C1F] border border-[#30363B]">
                <p className="text-2xl sm:text-3xl font-black text-[#81C784]">1.29M</p>
                <p className="text-[11px] text-[#A3ADB5] mt-0.5">{lang === 'ar' ? 'مبيعات التجارة الإلكترونية' : 'E-Commerce Sales'}</p>
              </div>
              <div className="p-4 rounded-xl bg-[#191C1F] border border-[#30363B]">
                <p className="text-2xl sm:text-3xl font-black text-[#FFB74D]">465K+</p>
                <p className="text-[11px] text-[#A3ADB5] mt-0.5">{lang === 'ar' ? 'وحدات طاقة إنتاجية' : 'Production Units'}</p>
              </div>
            </div>
          </section>

          {/* Projects Section */}
          <section id="projects" className="py-14 px-6 max-w-7xl mx-auto bg-[#111315]">
            <div className="text-center max-w-xl mx-auto mb-10">
              <span className="px-3 py-1 rounded-full bg-[#191C1F] border border-[#30363B] text-[#78A99B] text-xs font-semibold mb-1.5 inline-block">
                {lang === 'ar' ? 'مشاريع حية' : 'Case Studies'}
              </span>
              <h2 className="text-2xl font-extrabold text-[#F1F3F4]">
                {lang === 'ar' ? 'معرض لوحات القيادة والتحليلات المباشرة' : 'Interactive Analytics Case Studies'}
              </h2>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              
              {/* Project 1: Steam */}
              <div className="rounded-2xl bg-[#191C1F] border border-[#30363B] overflow-hidden flex flex-col hover:border-[#78A99B] transition-all">
                <img src={steamImg} alt="Steam" className="w-full h-48 object-cover object-top opacity-90" />
                <div className="p-5 flex-1 flex flex-col justify-between space-y-3">
                  <div>
                    <span className="px-2 py-0.5 rounded bg-[#202428] text-[#78A99B] border border-[#30363B] text-[10px] font-semibold uppercase mb-1.5 inline-block">Power BI & Excel</span>
                    <h3 className="text-base font-bold text-[#F1F3F4]">{lang === 'ar' ? 'دراسة وتحليل سوق الألعاب العالمي (Steam)' : 'Steam Games Market Analytics'}</h3>
                    <p className="text-xs text-[#A3ADB5] mt-1 leading-relaxed">
                      {lang === 'ar' ? 'تحليل شامل لـ 22,500+ لعبة و 5.7M+ لاعب متزامن ونسب التقييمات الإيجابية وسلوك المستخدمين.' : 'Comprehensive study over 22,500+ titles and 5.7M+ concurrent players.'}
                    </p>
                  </div>
                  <div className="flex gap-2">
                    <button onClick={() => setActiveModal('steam-analytics')} className="flex-1 py-2 rounded-xl bg-[#78A99B] hover:bg-[#8DBBAC] text-[#111315] font-bold text-xs shadow-sm">
                      📊 {lang === 'ar' ? 'عرض الداشبورد' : 'Open BI'}
                    </button>
                    <a href="Database.xlsx" download="Database.xlsx" className="py-2 px-3 rounded-xl bg-[#202428] hover:bg-[#252A2D] text-[#78A99B] border border-[#30363B] font-bold text-xs shadow-sm flex items-center justify-center">
                      📗 Excel
                    </a>
                  </div>
                </div>
              </div>

              {/* Project 2: Cost */}
              <div className="rounded-2xl bg-[#191C1F] border border-[#30363B] overflow-hidden flex flex-col hover:border-[#78A99B] transition-all">
                <img src={costImg} alt="Cost Variance" className="w-full h-48 object-cover object-top opacity-90" />
                <div className="p-5 flex-1 flex flex-col justify-between space-y-3">
                  <div>
                    <span className="px-2 py-0.5 rounded bg-[#202428] text-[#78A99B] border border-[#30363B] text-[10px] font-semibold uppercase mb-1.5 inline-block">Cost Accounting BI</span>
                    <h3 className="text-base font-bold text-[#F1F3F4]">{lang === 'ar' ? 'لوحة تحليل تكاليف الإنتاج وانحراف الكميات' : 'Manufacturing Cost Variance BI'}</h3>
                    <p className="text-xs text-[#A3ADB5] mt-1 leading-relaxed">
                      {lang === 'ar' ? 'تتبع طاقة إنتاجية بـ 465,165 قطعة وانحرافات كمية بـ 3,657 قطعة وتحليل المبيعات وأوامر الإنتاج.' : 'Tracking 465k capacity units, 3.6k quantity variance and product revenues.'}
                    </p>
                  </div>
                  <div className="flex gap-2">
                    <button onClick={() => setActiveModal('cost-variance')} className="flex-1 py-2 rounded-xl bg-[#78A99B] hover:bg-[#8DBBAC] text-[#111315] font-bold text-xs shadow-sm">
                      📊 {lang === 'ar' ? 'عرض الداشبورد' : 'Open BI'}
                    </button>
                    <a href="Production Order Visual Report.xlsx" download="Production Order Visual Report.xlsx" className="py-2 px-3 rounded-xl bg-[#202428] hover:bg-[#252A2D] text-[#78A99B] border border-[#30363B] font-bold text-xs shadow-sm flex items-center justify-center">
                      📗 Excel
                    </a>
                  </div>
                </div>
              </div>

              {/* Project 3: MISUO */}
              <div className="rounded-2xl bg-[#191C1F] border border-[#30363B] overflow-hidden flex flex-col hover:border-[#78A99B] transition-all">
                <img src={misuoImg} alt="MISUO BI" className="w-full h-48 object-cover object-top opacity-90" />
                <div className="p-5 flex-1 flex flex-col justify-between space-y-3">
                  <div>
                    <span className="px-2 py-0.5 rounded bg-[#202428] text-[#78A99B] border border-[#30363B] text-[10px] font-semibold uppercase mb-1.5 inline-block">E-Commerce & Logistics</span>
                    <h3 className="text-base font-bold text-[#F1F3F4]">{lang === 'ar' ? 'تحليل أداء مبيعات وسلاسل التوريد (MISUO)' : 'MISUO E-Commerce BI'}</h3>
                    <p className="text-xs text-[#A3ADB5] mt-1 leading-relaxed">
                      {lang === 'ar' ? 'تحليل 1.29M جنيه مبيعات عبر 152 طلباً وتوزيع المبيعات جغرافياً على محافظات مصر ونسب التسليم.' : 'Analyzing 1.29M EGP revenue across 152 orders with Egyptian regional delivery breakdown.'}
                    </p>
                  </div>
                  <div className="flex gap-2">
                    <button onClick={() => setActiveModal('misuo-ecommerce')} className="flex-1 py-2 rounded-xl bg-[#78A99B] hover:bg-[#8DBBAC] text-[#111315] font-bold text-xs shadow-sm">
                      📊 {lang === 'ar' ? 'عرض الداشبورد' : 'Open BI'}
                    </button>
                    <a href="MISUO - Abdelaziz Usama Mahmoud.xlsx" download="MISUO - Abdelaziz Usama Mahmoud.xlsx" className="py-2 px-3 rounded-xl bg-[#202428] hover:bg-[#252A2D] text-[#78A99B] border border-[#30363B] font-bold text-xs shadow-sm flex items-center justify-center">
                      📗 Excel
                    </a>
                  </div>
                </div>
              </div>

            </div>
          </section>

          {/* Footer */}
          <footer className="bg-[#111315] border-t border-[#30363B] py-6 text-center text-xs text-[#A3ADB5]">
            عبدالعزيز أسامة محمود © 2026 — جميع الحقوق محفوظة
          </footer>

          {/* Modal 1: Steam */}
          {activeModal === 'steam-analytics' && (
            <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md overflow-y-auto">
              <div className="relative w-full max-w-4xl bg-[#191C1F] border border-[#30363B] rounded-2xl p-5 space-y-5 max-h-[90vh] overflow-y-auto text-[#F1F3F4]">
                <div className="flex justify-between items-center border-b border-[#30363B] pb-3">
                  <h3 className="text-base font-bold text-[#F1F3F4]">🎮 {lang === 'ar' ? 'تحليل سوق الألعاب العالمي (Steam)' : 'Steam Games Analytics'}</h3>
                  <div className="flex items-center gap-2">
                    <a href="Database.xlsx" download="Database.xlsx" className="px-3 py-1 rounded bg-[#78A99B] text-[#111315] text-xs font-bold flex items-center gap-1">
                      📗 {lang === 'ar' ? 'تحميل ملف Excel' : 'Download Excel'}
                    </a>
                    <button onClick={() => setActiveModal(null)} className="w-7 h-7 rounded bg-[#202428] border border-[#30363B] text-[#A3ADB5]">✕</button>
                  </div>
                </div>

                <img src={steamImg} className="w-full h-56 object-cover object-top rounded-xl border border-[#30363B]" />

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div className="p-3.5 rounded-xl bg-[#202428] border border-[#30363B]">
                    <h4 className="text-xs font-bold text-[#78A99B] mb-2">أعلى 10 ألعاب جذباً للاعبين (CCU)</h4>
                    <div className="h-48"><canvas ref={steamCcURef}></canvas></div>
                  </div>
                  <div className="p-3.5 rounded-xl bg-[#202428] border border-[#30363B]">
                    <h4 className="text-xs font-bold text-[#81C784] mb-2">نسبة انطباعات التقييمات</h4>
                    <div className="h-48"><canvas ref={steamSentimentRef}></canvas></div>
                  </div>
                </div>

                {/* Table */}
                <div className="p-3.5 rounded-xl bg-[#202428] border border-[#30363B]">
                  <div className="flex justify-between items-center mb-2">
                    <h4 className="text-xs font-bold text-[#F1F3F4]">مستكشف داتا الألعاب التفاعلي</h4>
                    <input
                      type="text"
                      placeholder="ابحث باسم اللعبة..."
                      value={searchTerm}
                      onChange={(e) => setSearchTerm(e.target.value)}
                      className="px-2.5 py-1 rounded bg-[#191C1F] border border-[#30363B] text-xs text-[#F1F3F4]"
                    />
                  </div>
                  <div className="overflow-x-auto">
                    <table className="w-full text-right text-xs text-[#A3ADB5]">
                      <thead className="bg-[#191C1F] text-[#F1F3F4] uppercase text-[10px]">
                        <tr>
                          <th className="p-2">اللعبة</th>
                          <th className="p-2">المطور</th>
                          <th className="p-2">CCU</th>
                          <th className="p-2">السعر</th>
                        </tr>
                      </thead>
                      <tbody>
                        {filteredGames.slice(0, 8).map((g, idx) => (
                          <tr key={idx} className="border-b border-[#30363B] hover:bg-[#252A2D]">
                            <td className="p-2 font-bold text-[#F1F3F4]">{g.name}</td>
                            <td className="p-2 text-[#A3ADB5]">{g.developer}</td>
                            <td className="p-2 font-bold text-[#78A99B]">{g.ccu.toLocaleString()}</td>
                            <td className="p-2 font-mono">{g.is_free ? 'مجاني' : '$' + (g.price/100).toFixed(2)}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* Modal 2: Cost */}
          {activeModal === 'cost-variance' && (
            <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md overflow-y-auto">
              <div className="relative w-full max-w-4xl bg-[#191C1F] border border-[#30363B] rounded-2xl p-5 space-y-5 max-h-[90vh] overflow-y-auto text-[#F1F3F4]">
                <div className="flex justify-between items-center border-b border-[#30363B] pb-3">
                  <h3 className="text-base font-bold text-[#F1F3F4]">📐 {lang === 'ar' ? 'لوحة تحليل تكاليف الإنتاج وانحراف الكميات' : 'Manufacturing Cost Variance BI'}</h3>
                  <div className="flex items-center gap-2">
                    <a href="Production Order Visual Report.xlsx" download="Production Order Visual Report.xlsx" className="px-3 py-1 rounded bg-[#78A99B] text-[#111315] text-xs font-bold flex items-center gap-1">
                      📗 {lang === 'ar' ? 'تحميل ملف Excel' : 'Download Excel'}
                    </a>
                    <button onClick={() => setActiveModal(null)} className="w-7 h-7 rounded bg-[#202428] border border-[#30363B] text-[#A3ADB5]">✕</button>
                  </div>
                </div>

                <img src={costImg} className="w-full h-56 object-cover object-top rounded-xl border border-[#30363B]" />

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div className="p-3.5 rounded-xl bg-[#202428] border border-[#30363B]">
                    <h4 className="text-xs font-bold text-[#E57373] mb-2">أعلى المنتجات بها انحراف في الكمية</h4>
                    <div className="h-52"><canvas ref={costVarianceRef}></canvas></div>
                  </div>
                  <div className="p-3.5 rounded-xl bg-[#202428] border border-[#30363B]">
                    <h4 className="text-xs font-bold text-[#81C784] mb-2">أعلى المنتجات تحقيقاً للمبيعات</h4>
                    <div className="h-52"><canvas ref={costSalesRef}></canvas></div>
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* Modal 3: MISUO */}
          {activeModal === 'misuo-ecommerce' && (
            <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md overflow-y-auto">
              <div className="relative w-full max-w-4xl bg-[#191C1F] border border-[#30363B] rounded-2xl p-5 space-y-5 max-h-[90vh] overflow-y-auto text-[#F1F3F4]">
                <div className="flex justify-between items-center border-b border-[#30363B] pb-3">
                  <h3 className="text-base font-bold text-[#F1F3F4]">🛍️ {lang === 'ar' ? 'تحليل أداء مبيعات وسلاسل التوريد (MISUO)' : 'MISUO Logistics & Sales BI'}</h3>
                  <div className="flex items-center gap-2">
                    <a href="MISUO - Abdelaziz Usama Mahmoud.xlsx" download="MISUO - Abdelaziz Usama Mahmoud.xlsx" className="px-3 py-1 rounded bg-[#78A99B] text-[#111315] text-xs font-bold flex items-center gap-1">
                      📗 {lang === 'ar' ? 'تحميل ملف Excel' : 'Download Excel'}
                    </a>
                    <button onClick={() => setActiveModal(null)} className="w-7 h-7 rounded bg-[#202428] border border-[#30363B] text-[#A3ADB5]">✕</button>
                  </div>
                </div>

                <img src={misuoImg} className="w-full h-56 object-cover object-top rounded-xl border border-[#30363B]" />

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div className="p-3.5 rounded-xl bg-[#202428] border border-[#30363B]">
                    <h4 className="text-xs font-bold text-[#81C784] mb-2">تفاصيل التسليمات والتنفيذ</h4>
                    <div className="h-48"><canvas ref={misuoDeliveryRef}></canvas></div>
                  </div>
                  <div className="p-3.5 rounded-xl bg-[#202428] border border-[#30363B]">
                    <h4 className="text-xs font-bold text-[#78A99B] mb-2">توزيع الطلبات حسب المحافظة</h4>
                    <div className="h-48"><canvas ref={misuoAreaRef}></canvas></div>
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* Modal 4: Contact */}
          {activeModal === 'contact' && (
            <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md">
              <div className="relative w-full max-w-sm bg-[#191C1F] border border-[#30363B] rounded-2xl p-5 space-y-3 shadow-2xl text-[#F1F3F4]">
                <div className="flex justify-between items-center border-b border-[#30363B] pb-2.5">
                  <h3 className="text-sm font-bold text-[#F1F3F4]">✉️ التواصل مع عبدالعزيز أسامة</h3>
                  <button onClick={() => setActiveModal(null)} className="w-6 h-6 rounded bg-[#202428] border border-[#30363B] text-[#A3ADB5]">✕</button>
                </div>
                <p className="text-xs text-[#78A99B] font-semibold">abdelaziz.osama.analytics@gmail.com</p>
                <form onSubmit={(e) => { e.preventDefault(); setContactSubmitted(true); setTimeout(() => { setContactSubmitted(false); setActiveModal(null); }, 1500); }} className="space-y-2.5">
                  <input type="text" required placeholder="الاسم..." className="w-full p-2 rounded bg-[#202428] border border-[#30363B] text-xs text-[#F1F3F4]" />
                  <textarea rows={3} required placeholder="تفاصيل الرسالة..." className="w-full p-2 rounded bg-[#202428] border border-[#30363B] text-xs text-[#F1F3F4]"></textarea>
                  <button type="submit" className="w-full py-2 bg-[#78A99B] hover:bg-[#8DBBAC] text-[#111315] font-bold text-xs rounded-xl shadow-sm">
                    {contactSubmitted ? 'تم الإرسال بنجاح!' : 'إرسال الرسالة'}
                  </button>
                </form>
              </div>
            </div>
          )}

        </div>
      );
    }

    ReactDOM.createRoot(document.getElementById('root')).render(<App />);
  </script>
</body>
</html>'''

html_content = template.replace('__PROFILE_B64__', profile_b64)
html_content = html_content.replace('__STEAM_B64__', steam_b64)
html_content = html_content.replace('__COST_B64__', cost_b64)
html_content = html_content.replace('__MISUO_B64__', misuo_b64)

html_content = html_content.replace('__STEAM_DATA__', json.dumps(steam_data, ensure_ascii=False))
html_content = html_content.replace('__COST_DATA__', json.dumps(cost_data, ensure_ascii=False))
html_content = html_content.replace('__MISUO_DATA__', json.dumps(misuo_data, ensure_ascii=False))

with open(os.path.join(downloads, 'portfolio_abdelaziz.html'), 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(os.path.join(scratch, 'portfolio_abdelaziz.html'), 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Updated standalone portfolio_abdelaziz.html with Premium Minimal Dark UI palette!')
