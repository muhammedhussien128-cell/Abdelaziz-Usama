import React from 'react';
import { ExternalLink, CheckCircle2, BarChart2, FileSpreadsheet } from 'lucide-react';

export default function CaseStudyCard({ project, lang, onOpenModal }) {
  const getExcelPath = (id) => {
    if (id === 'steam-analytics') return { path: '/assets/Database_Steam_Games.xlsx', name: 'Database.xlsx' };
    if (id === 'cost-variance') return { path: '/assets/Production_Order_Visual_Report.xlsx', name: 'Production Order Visual Report.xlsx' };
    if (id === 'misuo-ecommerce') return { path: '/assets/MISUO_Abdelaziz_Usama_Mahmoud.xlsx', name: 'MISUO - Abdelaziz Usama Mahmoud.xlsx' };
    return null;
  };

  const excelInfo = getExcelPath(project.id);

  return (
    <div className="rounded-2xl bg-[#191C1F] border border-[#30363B] overflow-hidden flex flex-col group hover:bg-[#252A2D] hover:border-[#78A99B] transition-all duration-300 shadow-md">
      
      {/* Image Container */}
      <div className="relative h-56 overflow-hidden bg-[#111315]">
        <img
          src={project.image}
          alt={project.title}
          className="w-full h-full object-cover object-top transition-transform duration-500 group-hover:scale-103 opacity-90 group-hover:opacity-100"
        />

        {/* Overlay */}
        <div className="absolute inset-0 bg-gradient-to-t from-[#191C1F] via-[#191C1F]/20 to-transparent" />

        {/* Badge */}
        <div className="absolute top-3 right-3 flex items-center gap-1.5">
          <span className="px-2.5 py-1 rounded-lg bg-[#202428]/95 text-[#78A99B] border border-[#30363B] text-[11px] font-semibold">
            {project.badge}
          </span>
        </div>

        {/* Title Overlay */}
        <div className="absolute bottom-3 left-3 right-3">
          <span className="text-[10px] font-semibold text-[#A3ADB5] uppercase tracking-wider block mb-0.5">
            {project.category}
          </span>
          <h3 className="text-base font-bold text-[#F1F3F4] leading-snug">
            {project.title}
          </h3>
        </div>
      </div>

      {/* Card Body */}
      <div className="p-5 flex-1 flex flex-col justify-between space-y-4">
        
        {/* Description */}
        <p className="text-[#A3ADB5] text-xs leading-relaxed font-normal">
          {project.description}
        </p>

        {/* Highlights */}
        <div className="space-y-1.5">
          {project.highlights.map((item, i) => (
            <div key={i} className="flex items-start gap-2 text-xs text-[#A3ADB5]">
              <CheckCircle2 className="w-3.5 h-3.5 text-[#78A99B] flex-shrink-0 mt-0.5" />
              <span>{item}</span>
            </div>
          ))}
        </div>

        {/* Action Buttons */}
        <div className="pt-3 border-t border-[#30363B] flex items-center gap-2">
          
          <button
            onClick={() => onOpenModal(project.id)}
            className="flex-1 py-2.5 px-3 rounded-xl bg-[#78A99B] hover:bg-[#8DBBAC] text-[#111315] font-bold text-xs flex items-center justify-center gap-1.5 transition-all shadow-sm cursor-pointer"
          >
            <BarChart2 className="w-4 h-4 text-[#111315]" />
            <span>{lang === 'ar' ? 'عرض الداشبورد' : 'Open BI'}</span>
            <ExternalLink className="w-3 h-3 opacity-80" />
          </button>

          {excelInfo && (
            <a
              href={excelInfo.path}
              download={excelInfo.name}
              title={lang === 'ar' ? `تحميل ملف ${excelInfo.name}` : `Download ${excelInfo.name}`}
              className="py-2.5 px-3 rounded-xl bg-[#202428] hover:bg-[#252A2D] text-[#78A99B] border border-[#30363B] font-bold text-xs flex items-center justify-center gap-1 transition-all cursor-pointer"
            >
              <FileSpreadsheet className="w-4 h-4" />
              <span>Excel</span>
            </a>
          )}

        </div>

      </div>

    </div>
  );
}
