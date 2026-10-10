import React from 'react';
import { X, Calculator, AlertTriangle, TrendingUp, Building2, Download, FileSpreadsheet } from 'lucide-react';
import costData from '../data/cost_data.json';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';
import { Bar } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

export default function ProjectCostModal({ lang, onClose }) {
  const varianceChartData = {
    labels: costData.top_variance_products.map(p => p.name.length > 25 ? p.name.substring(0, 25) + '...' : p.name),
    datasets: [
      {
        label: lang === 'ar' ? 'انحراف الكمية (قطع)' : 'Quantity Variance (Units)',
        data: costData.top_variance_products.map(p => p.variance),
        backgroundColor: '#E57373',
        borderColor: '#EF5350',
        borderWidth: 1,
        borderRadius: 6
      }
    ]
  };

  const salesChartData = {
    labels: costData.top_sales_products.map(p => p.name.length > 25 ? p.name.substring(0, 25) + '...' : p.name),
    datasets: [
      {
        label: lang === 'ar' ? 'إجمالي المبيعات (جنية)' : 'Sales Revenue (EGP)',
        data: costData.top_sales_products.map(p => p.sales),
        backgroundColor: '#81C784',
        borderColor: '#66BB6A',
        borderWidth: 1,
        borderRadius: 6
      }
    ]
  };

  const companyOrdersData = {
    labels: costData.company_production_orders.map(c => c.company),
    datasets: [
      {
        label: lang === 'ar' ? 'عدد أوامر الإنتاج' : 'Production Orders',
        data: costData.company_production_orders.map(c => c.orders),
        backgroundColor: '#78A99B',
        borderColor: '#8DBBAC',
        borderWidth: 1,
        borderRadius: 6
      }
    ]
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md overflow-y-auto">
      <div className="relative w-full max-w-6xl bg-[#191C1F] border border-[#30363B] rounded-2xl shadow-2xl overflow-hidden my-8 max-h-[90vh] flex flex-col text-[#F1F3F4]">
        
        {/* Modal Header */}
        <div className="p-5 bg-[#202428] border-b border-[#30363B] flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-[#191C1F] border border-[#30363B] flex items-center justify-center">
              <Calculator className="w-5 h-5 text-[#78A99B]" />
            </div>
            <div>
              <h2 className="text-lg font-bold text-[#F1F3F4]">
                {lang === 'ar' ? 'لوحة تحليل تكاليف الإنتاج وانحراف الكميات' : 'Production Cost Variance & Capacity Analytics'}
              </h2>
              <p className="text-xs text-[#A3ADB5]">
                {lang === 'ar' ? 'تقرير أوامر الإنتاج البصري: Production Order Visual Report.xlsx' : 'Production Order Visual Report'}
              </p>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <a
              href="/assets/Production_Order_Visual_Report.xlsx"
              download="Production Order Visual Report.xlsx"
              className="hidden sm:flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-[#78A99B] hover:bg-[#8DBBAC] text-[#111315] text-xs font-bold transition-all"
            >
              <FileSpreadsheet className="w-4 h-4" />
              <span>{lang === 'ar' ? 'تحميل ملف Production Order.xlsx' : 'Download Excel File'}</span>
            </a>

            <button
              onClick={onClose}
              className="w-8 h-8 rounded-lg bg-[#191C1F] border border-[#30363B] text-[#A3ADB5] hover:text-[#F1F3F4] flex items-center justify-center"
            >
              <X className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* Modal Body */}
        <div className="p-6 space-y-6 overflow-y-auto custom-scrollbar flex-1 bg-[#111315]">
          
          {/* Snapshot */}
          <div className="relative rounded-xl overflow-hidden border border-[#30363B] bg-[#191C1F]">
            <img
              src="/assets/dashboard_cost.jpg"
              alt="Cost Accounting Dashboard Snapshot"
              className="w-full h-64 object-cover object-top opacity-95"
            />
            <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-[#111315] via-[#111315]/80 to-transparent p-4 flex justify-between items-center">
              <span className="text-xs font-semibold px-3 py-1 rounded bg-[#202428] text-[#78A99B] border border-[#30363B]">
                {lang === 'ar' ? 'محاسبة التكاليف الصناعية والانحرافات' : 'Industrial Cost Accounting & Variance'}
              </span>

              <a
                href="/assets/Production_Order_Visual_Report.xlsx"
                download="Production Order Visual Report.xlsx"
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-[#78A99B] hover:bg-[#8DBBAC] text-[#111315] text-xs font-bold shadow-sm"
              >
                <Download className="w-3.5 h-3.5" />
                <span>{lang === 'ar' ? 'تحميل ملف Production Order Visual Report.xlsx' : 'Download Production Order.xlsx'}</span>
              </a>
            </div>
          </div>

          {/* Key Metrics */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <div className="p-3.5 rounded-xl bg-[#191C1F] border border-[#30363B] text-center">
              <p className="text-xs text-[#A3ADB5] mb-1">{lang === 'ar' ? 'الطاقة الإنتاجية الزمانية' : 'Total Capacity of Production'}</p>
              <p className="text-2xl sm:text-3xl font-black text-[#78A99B]">465,165</p>
              <p className="text-[10px] text-[#A3ADB5] mt-0.5">{lang === 'ar' ? 'قطعة منتجة' : 'Units'}</p>
            </div>

            <div className="p-3.5 rounded-xl bg-[#191C1F] border border-[#30363B] text-center">
              <p className="text-xs text-[#A3ADB5] mb-1">{lang === 'ar' ? 'انحراف الكمية الإجمالي' : 'Total Quantity Variance'}</p>
              <p className="text-2xl sm:text-3xl font-black text-[#E57373]">3,657</p>
              <p className="text-[10px] text-[#A3ADB5] mt-0.5">{lang === 'ar' ? 'قطعة انحراف' : 'Units Variance'}</p>
            </div>

            <div className="p-3.5 rounded-xl bg-[#191C1F] border border-[#30363B] text-center">
              <p className="text-xs text-[#A3ADB5] mb-1">{lang === 'ar' ? 'شركات الإنتاج المتعاقدة' : 'Active Client Brands'}</p>
              <p className="text-2xl sm:text-3xl font-black text-[#F1F3F4]">18</p>
              <p className="text-[10px] text-[#A3ADB5] mt-0.5">{lang === 'ar' ? 'شركة مصنعة' : 'Companies'}</p>
            </div>
          </div>

          {/* Charts Row 1 */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div className="p-4 rounded-xl bg-[#191C1F] border border-[#30363B]">
              <h3 className="text-xs font-bold text-[#F1F3F4] mb-3 flex items-center gap-2">
                <AlertTriangle className="w-4 h-4 text-[#E57373]" />
                <span>{lang === 'ar' ? 'أكثر 10 منتجات بها انحراف في الكمية (High Variance)' : 'Top 10 High Variance Products'}</span>
              </h3>
              <div className="h-60">
                <Bar
                  data={varianceChartData}
                  options={{
                    indexAxis: 'y',
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: {
                      x: { ticks: { color: '#A3ADB5' }, grid: { color: '#30363B' } },
                      y: { ticks: { color: '#A3ADB5', font: { size: 10 } }, grid: { color: '#30363B' } }
                    }
                  }}
                />
              </div>
            </div>

            <div className="p-4 rounded-xl bg-[#191C1F] border border-[#30363B]">
              <h3 className="text-xs font-bold text-[#F1F3F4] mb-3 flex items-center gap-2">
                <TrendingUp className="w-4 h-4 text-[#81C784]" />
                <span>{lang === 'ar' ? 'أكثر 10 منتجات تحقيقاً للمبيعات (High Sales)' : 'Top 10 High Sales Products'}</span>
              </h3>
              <div className="h-60">
                <Bar
                  data={salesChartData}
                  options={{
                    indexAxis: 'y',
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: {
                      x: { ticks: { color: '#A3ADB5' }, grid: { color: '#30363B' } },
                      y: { ticks: { color: '#A3ADB5', font: { size: 10 } }, grid: { color: '#30363B' } }
                    }
                  }}
                />
              </div>
            </div>
          </div>

          {/* Chart Row 2 */}
          <div className="p-4 rounded-xl bg-[#191C1F] border border-[#30363B]">
            <h3 className="text-xs font-bold text-[#F1F3F4] mb-3 flex items-center gap-2">
              <Building2 className="w-4 h-4 text-[#78A99B]" />
              <span>{lang === 'ar' ? 'توزيع أوامر الإنتاج حسب الشركات (Company Production Orders)' : 'Production Orders Breakdown by Client Company'}</span>
            </h3>
            <div className="h-60">
              <Bar
                data={companyOrdersData}
                options={{
                  responsive: true,
                  maintainAspectRatio: false,
                  plugins: { legend: { display: false } },
                  scales: {
                    x: { ticks: { color: '#A3ADB5' }, grid: { color: '#30363B' } },
                    y: { ticks: { color: '#A3ADB5' }, grid: { color: '#30363B' } }
                  }
                }}
              />
            </div>
          </div>

        </div>

      </div>
    </div>
  );
}
