import React from 'react';
import { portfolioData } from '../data/portfolio_content';
import { Cpu, Calculator, Truck, CheckCircle2 } from 'lucide-react';

export default function SkillsSection({ lang }) {
  const skillGroups = portfolioData[lang].skills;

  const groupIcons = [
    <Cpu className="w-5 h-5 text-[#78A99B]" />,
    <Calculator className="w-5 h-5 text-[#78A99B]" />,
    <Truck className="w-5 h-5 text-[#78A99B]" />
  ];

  return (
    <section id="skills" className="py-14 relative z-10 bg-[#111315] border-y border-[#30363B]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Section Header */}
        <div className="text-center max-w-2xl mx-auto mb-10">
          <span className="px-3.5 py-1 rounded-full bg-[#191C1F] border border-[#30363B] text-[#78A99B] text-xs font-semibold mb-2 inline-block">
            {lang === 'ar' ? 'الخبرات الفنية والمحاسبية' : 'Core Capabilities'}
          </span>
          <h2 className="text-2xl font-extrabold text-[#F1F3F4] mb-2">
            {lang === 'ar' ? 'المهارات التقنية والتحليلية والمحاسبية' : 'Technical, Financial & Analytical Expertise'}
          </h2>
          <p className="text-[#A3ADB5] text-xs sm:text-sm">
            {lang === 'ar'
              ? 'مزيج فريد يجمع بين الدقة المحاسبية لتكاليف الإنتاج والقوة التقنية لأدوات الذكاء التجاري والبرمجة.'
              : 'A fusion of manufacturing cost precision and modern BI analytics execution.'}
          </p>
        </div>

        {/* Skill Category Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {skillGroups.map((group, idx) => (
            <div
              key={idx}
              className="p-5 rounded-2xl bg-[#191C1F] border border-[#30363B] shadow-sm hover:border-[#78A99B] transition-all"
            >
              <div className="flex items-center gap-3 mb-4 pb-3 border-b border-[#30363B]">
                <div className="w-9 h-9 rounded-xl bg-[#202428] border border-[#30363B] flex items-center justify-center">
                  {groupIcons[idx]}
                </div>
                <h3 className="text-sm font-bold text-[#F1F3F4]">
                  {group.category}
                </h3>
              </div>

              {/* Items List */}
              <div className="space-y-2.5">
                {group.items.map((item, i) => (
                  <div key={i} className="flex items-center justify-between p-2.5 rounded-xl bg-[#202428] border border-[#30363B]">
                    <div className="flex items-center gap-2">
                      <CheckCircle2 className="w-3.5 h-3.5 text-[#78A99B] flex-shrink-0" />
                      <span className="text-xs font-semibold text-[#F1F3F4]">{item}</span>
                    </div>
                    <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-[#191C1F] text-[#78A99B] border border-[#30363B]">
                      {lang === 'ar' ? 'متقن' : 'Expert'}
                    </span>
                  </div>
                ))}
              </div>

            </div>
          ))}
        </div>

      </div>
    </section>
  );
}
