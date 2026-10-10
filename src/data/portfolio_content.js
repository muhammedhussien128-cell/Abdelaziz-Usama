export const portfolioData = {
  en: {
    personal: {
      name: "Abdelaziz Osama Mahmoud",
      title: "Senior Data Analyst & Business Intelligence Specialist | Cost Accountant",
      tagline: "Transforming complex operational & financial data into executive strategic dashboards and profitable business decisions.",
      bio: "Senior Data Analyst & BI Specialist with advanced experience integrating Cost Accounting, Manufacturing Operations, and Supply Chain Logistics with Business Intelligence. Proven track record in architecting executive interactive dashboards, quantity variance modeling, e-commerce fulfillment analytics, and big-data game market research.",
      location: "Cairo, Egypt",
      email: "abdelaziz.osama.analytics@gmail.com",
      phone: "+20 100 000 0000",
      linkedin: "https://linkedin.com/in/abdelaziz-osama-data",
      github: "https://github.com/abdelaziz-data",
    },
    stats: [
      { label: "Data Records Analyzed", value: "22,524", suffix: "Titles" },
      { label: "Steam Concurrent Players", value: "5.7M+", suffix: "CCU" },
      { label: "E-Commerce Revenue Modeled", value: "1.29M", suffix: "EGP" },
      { label: "Production Units Tracked", value: "465K+", suffix: "Units" }
    ],
    skills: [
      { 
        category: "Business Intelligence & Analytics", 
        items: ["Power BI & DAX Modeling", "Power Query & ETL", "Data Architecture", "Python (Pandas, NumPy)", "SQL Database Querying", "Executive Dashboards"] 
      },
      { 
        category: "Financial & Cost Accounting", 
        items: ["Quantity Variance Analysis", "Product Cost Allocation", "Financial Modeling & Pricing", "Budgeting & Forecasting", "Managerial Reporting", "Excel Visual Reports & VBA"] 
      },
      { 
        category: "Operations & Logistics BI", 
        items: ["On-Time Delivery (SLA)", "Sales Channel Distribution", "Inventory & Storage Analytics", "Regional Demand Mapping", "Order Cancellation Analysis", "Supply Chain Optimization"] 
      }
    ],
    projects: [
      {
        id: "steam-analytics",
        title: "Steam Gaming Industry Market Intelligence & Player Engagement Analysis",
        category: "Big Data & Market Analytics",
        badge: "Power BI & Excel Report",
        image: "/assets/dashboard_steam.jpg",
        excelFile: "Database.xlsx",
        excelPath: "/assets/Database_Steam_Games.xlsx",
        description: "Comprehensive analytical study of 22,524 game titles on the Steam platform, tracking 5.7M+ concurrent users (CCU), sentiment breakdown, platform OS distribution (Windows, Mac, Linux), and free vs paid monetization models.",
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
        image: "/assets/dashboard_cost.jpg",
        excelFile: "Production Order Visual Report.xlsx",
        excelPath: "/assets/Production_Order_Visual_Report.xlsx",
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
        image: "/assets/dashboard_misuo.jpg",
        excelFile: "MISUO - Abdelaziz Usama Mahmoud.xlsx",
        excelPath: "/assets/MISUO_Abdelaziz_Usama_Mahmoud.xlsx",
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
      title: "محلل بيانات أول ومختص الذكاء التجاري (BI Specialist) | محاسب تكاليف",
      tagline: "تحويل البيانات المبعثرة والمعقدة إلى قرارات استراتيجية مربحة ولوحات قيادة تفاعلية مذهلة.",
      bio: "محلل بيانات محترف ذو خبرة متقدمة في ربط التحليل المالي وتحليل التكاليف بذكاء الأعمال (Business Intelligence). متمكن في تصميم وتطوير لوحات القيادة التفاعلية (Dashboards) لتتبع الأداء المالي والإنتاجي، وتحليل انحراف الكميات والتكاليف الصناعية، وتتبع سلاسل الإمداد ومبيعات التجارة الإلكترونية.",
      location: "القاهرة، مصر",
      email: "abdelaziz.osama.analytics@gmail.com",
      phone: "+20 100 000 0000",
      linkedin: "https://linkedin.com/in/abdelaziz-osama-data",
      github: "https://github.com/abdelaziz-data",
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
        image: "/assets/dashboard_steam.jpg",
        excelFile: "Database.xlsx",
        excelPath: "/assets/Database_Steam_Games.xlsx",
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
        image: "/assets/dashboard_cost.jpg",
        excelFile: "Production Order Visual Report.xlsx",
        excelPath: "/assets/Production_Order_Visual_Report.xlsx",
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
        title: "تحليل أداء مبيعات وسلاسل التوريد لشركة MISUO للتجارة الإلكترونية",
        category: "التجارة الإلكترونية واللوجستيات",
        badge: "MISUO Executive Dashboard",
        image: "/assets/dashboard_misuo.jpg",
        excelFile: "MISUO - Abdelaziz Usama Mahmoud.xlsx",
        excelPath: "/assets/MISUO_Abdelaziz_Usama_Mahmoud.xlsx",
        description: "تحليل متكامل لعمليات البيع والتوصيل لشركة MISUO بإجمالي مبيعات 1,292,886 جنيه عبر 152 طلباً. يركز المشروع على قياس كفاءة شركات الشحن والتسليم والألوان والأشكال الأكثر مبيعاً مبعثرة جغرافياً على محافظات مصر.",
        highlights: [
          "تحليل إجمالي مبيعات بقيمة 1,292,886 ج.م بمتوسط قيمة طلب 10,261 ج.م.",
          "تصدر محافظة القاهرة لأعلى المحافظات شراءً بـ 60 طلباً تليهما الجيزة (24) والقليوبية (11).",
          "تحليل قنوات البيع: تصدر منصة HomeMart بـ 94 وحدة مباعة، تليه منصة السويس و تاكي.",
          "تقييم كفاءة التوصيل: نسبة التسليم الناجح 81%، ونسبة المرفوضات والملغاة 18%."
        ]
      }
    ]
  }
};
