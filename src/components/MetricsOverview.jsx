import React from 'react';
import { portfolioData } from '../data/portfolio_content';
import { Database, Users, DollarSign, PackageCheck, Zap } from 'lucide-react';

export default function MetricsOverview({ lang }) {
  const stats = portfolioData[lang].stats;

  const icons = [
    <Database className="w-5 h-5 text-[#78A99B]" />,
    <Users className="w-5 h-5 text-[#78A99B]" />,
    <DollarSign className="w-5 h-5 text-[#78A99B]" />,
    <PackageCheck className="w-5 h-5 text-[#78A99B]" />
  ];

  return (
    <section id="metrics" className="py-10 relative z-10 bg-[#111315]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Title */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#191C1F] border border-[#30363B] text-[#78A99B] text-xs font-semibold mb-2">
            <Zap className="w-3.5 h-3.5" />
            <span>{lang === 'ar' ? 'ملخص الأرقام والتأثير' : 'Impact Metrics'}</span>
          </div>
          <h2 className="text-xl sm:text-2xl font-bold text-[#F1F3F4]">
            {lang === 'ar' ? 'إحصائيات وقدرات معالجة البيانات' : 'Data Scale & Processing Capacity'}
          </h2>
        </div>

        {/* Stats Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
          {stats.map((stat, idx) => (
            <div
              key={idx}
              className="p-5 rounded-2xl bg-[#191C1F] border border-[#30363B] shadow-sm hover:bg-[#252A2D] hover:border-[#78A99B] transition-all"
            >
              <div className="flex items-center justify-between mb-3">
                <div className="w-10 h-10 rounded-xl bg-[#202428] border border-[#30363B] flex items-center justify-center">
                  {icons[idx]}
                </div>
                <span className="text-[11px] font-semibold px-2 py-0.5 rounded-full bg-[#202428] text-[#A3ADB5] border border-[#30363B]">
                  {stat.suffix}
                </span>
              </div>

              <h3 className="text-2xl sm:text-3xl font-black text-[#F1F3F4] tracking-tight mb-1">
                {stat.value}
              </h3>
              
              <p className="text-xs text-[#A3ADB5] font-medium">
                {stat.label}
              </p>
            </div>
          ))}
        </div>

      </div>
    </section>
  );
}
