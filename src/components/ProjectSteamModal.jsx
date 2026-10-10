import React, { useState } from 'react';
import { X, Search, Gamepad2, ThumbsUp, Download, FileSpreadsheet } from 'lucide-react';
import steamData from '../data/steam_data.json';
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

export default function ProjectSteamModal({ lang, onClose }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [freeFilter, setFreeFilter] = useState('all');

  const topCcuData = {
    labels: steamData.top_ccu.map(g => g.name.length > 20 ? g.name.substring(0, 20) + '...' : g.name),
    datasets: [
      {
        label: lang === 'ar' ? 'عدد اللاعبين المتزامنين (CCU)' : 'Concurrent Players (CCU)',
        data: steamData.top_ccu.map(g => g.ccu),
        backgroundColor: '#78A99B',
        borderColor: '#8DBBAC',
        borderWidth: 1,
        borderRadius: 6
      }
    ]
  };

  const sentimentData = {
    labels: [
      lang === 'ar' ? 'تقييمات إيجابية (86%)' : 'Positive Reviews (86%)',
      lang === 'ar' ? 'تقييمات سلبية (14%)' : 'Negative Reviews (14%)'
    ],
    datasets: [
      {
        data: [steamData.total_positive, steamData.total_negative],
        backgroundColor: ['#81C784', '#E57373'],
        borderWidth: 0
      }
    ]
  };

  const filteredGames = steamData.sample_games.filter(g => {
    const matchesSearch = g.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                          g.developer.toLowerCase().includes(searchTerm.toLowerCase());
    if (freeFilter === 'free') return matchesSearch && g.is_free;
    if (freeFilter === 'paid') return matchesSearch && !g.is_free;
    return matchesSearch;
  });

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md overflow-y-auto">
      <div className="relative w-full max-w-6xl bg-[#191C1F] border border-[#30363B] rounded-2xl shadow-2xl overflow-hidden my-8 max-h-[90vh] flex flex-col text-[#F1F3F4]">
        
        {/* Modal Header */}
        <div className="p-5 bg-[#202428] border-b border-[#30363B] flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-[#191C1F] border border-[#30363B] flex items-center justify-center">
              <Gamepad2 className="w-5 h-5 text-[#78A99B]" />
            </div>
            <div>
              <h2 className="text-lg font-bold text-[#F1F3F4]">
                {lang === 'ar' ? 'تحليل سوق الألعاب العالمي على منصة Steam' : 'Steam Games Global Market Analytics'}
              </h2>
              <p className="text-xs text-[#A3ADB5]">
                {lang === 'ar' ? 'دراسة وإحصائيات أكثر من 22,500 لعبة و 5.7M+ لاعب متزامن' : 'Comprehensive study over 22,500+ titles & 5.7M+ concurrent players'}
              </p>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <a
              href="/assets/Database_Steam_Games.xlsx"
              download="Database.xlsx"
              className="hidden sm:flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-[#78A99B] hover:bg-[#8DBBAC] text-[#111315] text-xs font-bold transition-all"
            >
              <FileSpreadsheet className="w-4 h-4" />
              <span>{lang === 'ar' ? 'تحميل ملف Database.xlsx' : 'Download Database.xlsx'}</span>
            </a>

            <button
              onClick={onClose}
              className="w-8 h-8 rounded-lg bg-[#191C1F] border border-[#30363B] text-[#A3ADB5] hover:text-[#F1F3F4] flex items-center justify-center"
            >
              <X className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* Modal Content */}
        <div className="p-6 space-y-6 overflow-y-auto custom-scrollbar flex-1 bg-[#111315]">
          
          {/* Snapshot */}
          <div className="relative rounded-xl overflow-hidden border border-[#30363B] bg-[#191C1F]">
            <img
              src="/assets/dashboard_steam.jpg"
              alt="Steam Dashboard Snapshot"
              className="w-full h-64 object-cover object-top opacity-95"
            />
            <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-[#111315] via-[#111315]/80 to-transparent p-4 flex justify-between items-center">
              <span className="text-xs font-semibold px-3 py-1 rounded bg-[#202428] text-[#78A99B] border border-[#30363B]">
                {lang === 'ar' ? 'صورة الداشبورد الأصلي من Power BI / Excel' : 'Original Dashboard Snapshot'}
              </span>

              <a
                href="/assets/Database_Steam_Games.xlsx"
                download="Database.xlsx"
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-[#78A99B] hover:bg-[#8DBBAC] text-[#111315] text-xs font-bold shadow-sm"
              >
                <Download className="w-3.5 h-3.5" />
                <span>{lang === 'ar' ? 'تحميل ملف Excel المصدر' : 'Download Excel'}</span>
              </a>
            </div>
          </div>

          {/* Key Metrics */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
            <div className="p-3.5 rounded-xl bg-[#191C1F] border border-[#30363B] text-center">
              <p className="text-xs text-[#A3ADB5] mb-1">{lang === 'ar' ? 'إجمالي الألعاب' : 'Total Games'}</p>
              <p className="text-2xl font-black text-[#F1F3F4]">22,524</p>
            </div>
            <div className="p-3.5 rounded-xl bg-[#191C1F] border border-[#30363B] text-center">
              <p className="text-xs text-[#A3ADB5] mb-1">{lang === 'ar' ? 'لاعبين متزامنين (CCU)' : 'Total CCU'}</p>
              <p className="text-2xl font-black text-[#78A99B]">5,705,135</p>
            </div>
            <div className="p-3.5 rounded-xl bg-[#191C1F] border border-[#30363B] text-center">
              <p className="text-xs text-[#A3ADB5] mb-1">{lang === 'ar' ? 'التقييمات الإيجابية' : 'Positive Ratio'}</p>
              <p className="text-2xl font-black text-[#81C784]">86%</p>
            </div>
            <div className="p-3.5 rounded-xl bg-[#191C1F] border border-[#30363B] text-center">
              <p className="text-xs text-[#A3ADB5] mb-1">{lang === 'ar' ? 'متوسط العمر' : 'Average Age'}</p>
              <p className="text-2xl font-black text-[#F1F3F4]">16.36 {lang === 'ar' ? 'عام' : 'years'}</p>
            </div>
          </div>

          {/* Charts */}
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
            <div className="lg:col-span-8 p-4 rounded-xl bg-[#191C1F] border border-[#30363B]">
              <h3 className="text-xs font-bold text-[#F1F3F4] mb-3 flex items-center gap-2">
                <Gamepad2 className="w-4 h-4 text-[#78A99B]" />
                <span>{lang === 'ar' ? 'أعلى 10 ألعاب جذباً للاعبين المتزامنين (High CCU)' : 'Top 10 Games by High CCU'}</span>
              </h3>
              <div className="h-60">
                <Bar
                  data={topCcuData}
                  options={{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: {
                      x: { ticks: { color: '#A3ADB5', font: { size: 10 } }, grid: { color: '#30363B' } },
                      y: { ticks: { color: '#A3ADB5' }, grid: { color: '#30363B' } }
                    }
                  }}
                />
              </div>
            </div>

            <div className="lg:col-span-4 p-4 rounded-xl bg-[#191C1F] border border-[#30363B] flex flex-col justify-between">
              <h3 className="text-xs font-bold text-[#F1F3F4] mb-3 flex items-center gap-2">
                <ThumbsUp className="w-4 h-4 text-[#81C784]" />
                <span>{lang === 'ar' ? 'نسبة انطباعات التقييمات' : 'Review Sentiment Ratio'}</span>
              </h3>
              <div className="h-52 flex items-center justify-center">
                <Doughnut
                  data={sentimentData}
                  options={{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { position: 'bottom', labels: { color: '#A3ADB5' } } }
                  }}
                />
              </div>
            </div>
          </div>

          {/* Table */}
          <div className="p-4 rounded-xl bg-[#191C1F] border border-[#30363B]">
            <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 mb-3">
              <div>
                <h3 className="text-xs font-bold text-[#F1F3F4] flex items-center gap-2">
                  <Search className="w-4 h-4 text-[#78A99B]" />
                  <span>{lang === 'ar' ? 'مستكشف بيانات الألعاب التفاعلي' : 'Interactive Games Explorer'}</span>
                </h3>
              </div>

              <div className="flex items-center gap-2">
                <input
                  type="text"
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  placeholder={lang === 'ar' ? 'ابحث باسم اللعبة...' : 'Search title...'}
                  className="px-3 py-1.5 rounded-lg bg-[#202428] border border-[#30363B] text-xs text-[#F1F3F4] placeholder-[#A3ADB5] focus:outline-none focus:border-[#78A99B]"
                />

                <select
                  value={freeFilter}
                  onChange={(e) => setFreeFilter(e.target.value)}
                  className="px-3 py-1.5 rounded-lg bg-[#202428] border border-[#30363B] text-xs text-[#F1F3F4] focus:outline-none focus:border-[#78A99B]"
                >
                  <option value="all">{lang === 'ar' ? 'الكل' : 'All'}</option>
                  <option value="free">{lang === 'ar' ? 'مجاني' : 'Free'}</option>
                  <option value="paid">{lang === 'ar' ? 'مدفوع' : 'Paid'}</option>
                </select>
              </div>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-right text-xs text-[#A3ADB5]">
                <thead className="bg-[#202428] text-[#F1F3F4] uppercase text-[10px]">
                  <tr>
                    <th className="px-3 py-2">{lang === 'ar' ? 'اسم اللعبة' : 'Title'}</th>
                    <th className="px-3 py-2">{lang === 'ar' ? 'المطور' : 'Developer'}</th>
                    <th className="px-3 py-2">{lang === 'ar' ? 'اللاعبين (CCU)' : 'CCU'}</th>
                    <th className="px-3 py-2">{lang === 'ar' ? 'السعر' : 'Price'}</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-[#30363B]">
                  {filteredGames.slice(0, 10).map((game, i) => (
                    <tr key={i} className="hover:bg-[#252A2D] transition-colors">
                      <td className="px-3 py-2 font-bold text-[#F1F3F4]">{game.name}</td>
                      <td className="px-3 py-2 text-[#A3ADB5]">{game.developer}</td>
                      <td className="px-3 py-2 font-semibold text-[#78A99B]">{game.ccu.toLocaleString()}</td>
                      <td className="px-3 py-2">
                        {game.is_free ? (
                          <span className="px-2 py-0.5 rounded bg-[#202428] text-[#81C784] font-bold border border-[#30363B]">FREE</span>
                        ) : (
                          <span className="font-mono font-bold text-[#F1F3F4]">${(game.price / 100).toFixed(2)}</span>
                        )}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

          </div>

        </div>

      </div>
    </div>
  );
}
