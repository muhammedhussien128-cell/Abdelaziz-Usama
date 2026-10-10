import React from 'react';
import { X, ShoppingBag, Truck, MapPin, Download, ShoppingCart, FileSpreadsheet } from 'lucide-react';
import misuoData from '../data/misuo_data.json';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
  ArcElement
} from 'chart.js';
import { Bar, Doughnut } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
  ArcElement
);

export default function ProjectMisuoModal({ lang, onClose }) {
  const deliveryData = {
    labels: misuoData.delivery_breakdown.map(d => `${d.status} (${d.percentage}%)`),
    datasets: [
      {
        data: misuoData.delivery_breakdown.map(d => d.percentage),
        backgroundColor: ['#81C784', '#FFB74D', '#E57373'],
        borderWidth: 0
      }
    ]
  };

  const areaData = {
    labels: misuoData.orders_by_area.map(a => a.city),
    datasets: [
      {
        label: lang === 'ar' ? 'عدد الطلبات حسب المحافظة' : 'Orders Count',
        data: misuoData.orders_by_area.map(a => a.orders),
        backgroundColor: '#78A99B',
        borderColor: '#8DBBAC',
        borderWidth: 1,
        borderRadius: 6
      }
    ]
  };

  const platformData = {
    labels: misuoData.sales_by_platform.map(p => p.platform),
    datasets: [
      {
        label: lang === 'ar' ? 'المنتجات المباعة حسب المنصة' : 'Units Sold per Platform',
        data: misuoData.sales_by_platform.map(p => p.units),
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
              <ShoppingBag className="w-5 h-5 text-[#78A99B]" />
            </div>
            <div>
              <h2 className="text-lg font-bold text-[#F1F3F4]">
                {lang === 'ar' ? 'لوحة تحليل أداء مبيعات وسلاسل التوريد لشركة مسيو (MISUO Dashboard)' : 'MISUO E-Commerce & Delivery Performance BI'}
              </h2>
              <p className="text-xs text-[#A3ADB5]">
                {lang === 'ar' ? 'ملف التتقرير المصدر: MISUO - Abdelaziz Usama Mahmoud.xlsx' : 'MISUO - Abdelaziz Usama Mahmoud.xlsx'}
              </p>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <a
              href="/assets/MISUO_Abdelaziz_Usama_Mahmoud.xlsx"
              download="MISUO - Abdelaziz Usama Mahmoud.xlsx"
              className="hidden sm:flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-[#78A99B] hover:bg-[#8DBBAC] text-[#111315] text-xs font-bold transition-all"
            >
              <FileSpreadsheet className="w-4 h-4" />
              <span>{lang === 'ar' ? 'تحميل ملف MISUO.xlsx' : 'Download Excel File'}</span>
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
              src="/assets/dashboard_misuo.jpg"
              alt="MISUO E-Commerce Dashboard Snapshot"
              className="w-full h-64 object-cover object-top opacity-95"
            />
            <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-[#111315] via-[#111315]/80 to-transparent p-4 flex justify-between items-center">
              <span className="text-xs font-semibold px-3 py-1 rounded bg-[#202428] text-[#78A99B] border border-[#30363B]">
                {lang === 'ar' ? 'تحليل المبيعات والتسليمات | شركة مسيو' : 'MISUO Sales & Logistics BI'}
              </span>

              <a
                href="/assets/MISUO_Abdelaziz_Usama_Mahmoud.xlsx"
                download="MISUO - Abdelaziz Usama Mahmoud.xlsx"
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-[#78A99B] hover:bg-[#8DBBAC] text-[#111315] text-xs font-bold shadow-sm"
              >
                <Download className="w-3.5 h-3.5" />
                <span>{lang === 'ar' ? 'تحميل ملف MISUO.xlsx' : 'Download MISUO.xlsx'}</span>
              </a>
            </div>
          </div>

          {/* Key Metrics */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
            <div className="p-3.5 rounded-xl bg-[#191C1F] border border-[#30363B] text-center">
              <p className="text-xs text-[#A3ADB5] mb-1">{lang === 'ar' ? 'إجمالي المبيعات' : 'Total Revenue'}</p>
              <p className="text-2xl sm:text-3xl font-black text-[#81C784]">1,292,886</p>
              <p className="text-[10px] text-[#A3ADB5] mt-0.5">EGP</p>
            </div>

            <div className="p-3.5 rounded-xl bg-[#191C1F] border border-[#30363B] text-center">
              <p className="text-xs text-[#A3ADB5] mb-1">{lang === 'ar' ? 'إجمالي الطلبات' : 'Total Orders'}</p>
              <p className="text-2xl sm:text-3xl font-black text-[#F1F3F4]">152</p>
              <p className="text-[10px] text-[#A3ADB5] mt-0.5">{lang === 'ar' ? 'طلب' : 'Orders'}</p>
            </div>

            <div className="p-3.5 rounded-xl bg-[#191C1F] border border-[#30363B] text-center">
              <p className="text-xs text-[#A3ADB5] mb-1">{lang === 'ar' ? 'متوسط سعر البيع' : 'Avg Selling Price'}</p>
              <p className="text-2xl sm:text-3xl font-black text-[#78A99B]">10,261</p>
              <p className="text-[10px] text-[#A3ADB5] mt-0.5">EGP</p>
            </div>

            <div className="p-3.5 rounded-xl bg-[#191C1F] border border-[#30363B] text-center">
              <p className="text-xs text-[#A3ADB5] mb-1">{lang === 'ar' ? 'المدينة الأكثر مبيعاً' : 'Top Sales City'}</p>
              <p className="text-2xl sm:text-3xl font-black text-[#F1F3F4]">القاهرة</p>
              <p className="text-[10px] text-[#A3ADB5] mt-0.5">60 {lang === 'ar' ? 'طلب' : 'Orders'}</p>
            </div>
          </div>

          {/* Charts Row 1 */}
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
            <div className="lg:col-span-4 p-4 rounded-xl bg-[#191C1F] border border-[#30363B] flex flex-col justify-between">
              <h3 className="text-xs font-bold text-[#F1F3F4] mb-3 flex items-center gap-2">
                <Truck className="w-4 h-4 text-[#81C784]" />
                <span>{lang === 'ar' ? 'حالة التوصيل والتسليمات' : 'Delivery Fulfillment Breakdown'}</span>
              </h3>
              <div className="h-52 flex items-center justify-center">
                <Doughnut
                  data={deliveryData}
                  options={{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { position: 'bottom', labels: { color: '#A3ADB5' } } }
                  }}
                />
              </div>
            </div>

            <div className="lg:col-span-8 p-4 rounded-xl bg-[#191C1F] border border-[#30363B]">
              <h3 className="text-xs font-bold text-[#F1F3F4] mb-3 flex items-center gap-2">
                <MapPin className="w-4 h-4 text-[#78A99B]" />
                <span>{lang === 'ar' ? 'توزيع الطلبات حسب المحافظة (Orders by Area)' : 'Regional Demand by Governorate'}</span>
              </h3>
              <div className="h-60">
                <Bar
                  data={areaData}
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

          {/* Platform Sales */}
          <div className="p-4 rounded-xl bg-[#191C1F] border border-[#30363B]">
            <h3 className="text-xs font-bold text-[#F1F3F4] mb-3 flex items-center gap-2">
              <ShoppingCart className="w-4 h-4 text-[#78A99B]" />
              <span>{lang === 'ar' ? 'عدد المنتجات المباعة حسب منصة البيع (Sales by Platform)' : 'Sales Volume by Retail Channel'}</span>
            </h3>
            <div className="h-56">
              <Bar
                data={platformData}
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
