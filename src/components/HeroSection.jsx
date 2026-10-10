import React from 'react';
import { portfolioData } from '../data/portfolio_content';
import { TrendingUp, Database, FileSpreadsheet, Award, ChevronRight, Mail, MapPin, Download } from 'lucide-react';

export default function HeroSection({ lang, onExploreProjects, onOpenContact }) {
  const content = portfolioData[lang].personal;

  return (
    <section id="about" className="relative pt-8 pb-16 overflow-hidden bg-[#111315]">
      
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center">
          
          {/* Text Column */}
          <div className="lg:col-span-8 text-right">
            
            {/* Status Badge */}
            <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-[#191C1F] border border-[#30363B] text-[#78A99B] text-xs font-semibold mb-4">
              <span className="w-2 h-2 rounded-full bg-[#78A99B]" />
              <span>{lang === 'ar' ? 'خبير تحليل البيانات والذكاء التجاري ومحاسبة التكاليف' : 'Data Analytics & Cost Accounting Expert'}</span>
            </div>

            {/* Main Name */}
            <h1 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight mb-3 text-[#F1F3F4] leading-tight">
              {content.name}
            </h1>

            {/* Role Title */}
            <p className="text-lg sm:text-2xl font-bold text-[#78A99B] mb-4 leading-snug">
              {content.title}
            </p>

            {/* Description */}
            <p className="text-[#A3ADB5] text-sm sm:text-base leading-relaxed mb-6 max-w-3xl font-normal">
              {content.bio}
            </p>

            {/* Skill Pills */}
            <div className="flex flex-wrap gap-2 mb-8">
              <span className="px-3 py-1.5 rounded-lg bg-[#191C1F] border border-[#30363B] text-xs font-semibold text-[#F1F3F4] flex items-center gap-1.5">
                <FileSpreadsheet className="w-3.5 h-3.5 text-[#78A99B]" />
                Excel Dashboards & Visual Reports
              </span>
              <span className="px-3 py-1.5 rounded-lg bg-[#191C1F] border border-[#30363B] text-xs font-semibold text-[#F1F3F4] flex items-center gap-1.5">
                <TrendingUp className="w-3.5 h-3.5 text-[#78A99B]" />
                Power BI & DAX
              </span>
              <span className="px-3 py-1.5 rounded-lg bg-[#191C1F] border border-[#30363B] text-xs font-semibold text-[#F1F3F4] flex items-center gap-1.5">
                <Database className="w-3.5 h-3.5 text-[#78A99B]" />
                Python & SQL Analytics
              </span>
              <span className="px-3 py-1.5 rounded-lg bg-[#191C1F] border border-[#30363B] text-xs font-semibold text-[#F1F3F4] flex items-center gap-1.5">
                <Award className="w-3.5 h-3.5 text-[#78A99B]" />
                Cost Variance Analysis
              </span>
            </div>

            {/* Action CTAs */}
            <div className="flex flex-wrap items-center gap-3">
              
              {/* Explore Dashboards */}
              <button
                onClick={onExploreProjects}
                className="px-5 py-3 rounded-xl bg-[#78A99B] hover:bg-[#8DBBAC] text-[#111315] font-bold text-xs sm:text-sm flex items-center gap-2 transition-all cursor-pointer shadow-sm"
              >
                <span>{lang === 'ar' ? 'استكشف لوحات القيادة (Dashboards)' : 'Explore Live Dashboards'}</span>
                <ChevronRight className="w-4 h-4 rotate-180" />
              </button>

              {/* Download Resume PDF */}
              <a
                href="/assets/Abdelaziz_Resume.pdf"
                download="Abdelaziz Usama Mahmoud Abdelaziz Resume.pdf"
                target="_blank"
                rel="noopener noreferrer"
                className="px-5 py-3 rounded-xl bg-[#202428] hover:bg-[#252A2D] text-[#F1F3F4] border border-[#30363B] font-bold text-xs sm:text-sm flex items-center gap-2 transition-all cursor-pointer"
              >
                <Download className="w-4 h-4 text-[#78A99B]" />
                <span>{lang === 'ar' ? 'تحميل السيرة الذاتية (CV PDF)' : 'Download Resume (PDF)'}</span>
              </a>

              {/* Contact Button */}
              <button
                onClick={onOpenContact}
                className="px-5 py-3 rounded-xl bg-[#191C1F] hover:bg-[#252A2D] text-[#A3ADB5] hover:text-[#F1F3F4] font-semibold text-xs sm:text-sm border border-[#30363B] flex items-center gap-2 transition-all cursor-pointer"
              >
                <Mail className="w-4 h-4 text-[#78A99B]" />
                <span>{lang === 'ar' ? 'تواصل معي مباشرة' : 'Get In Touch'}</span>
              </button>
            </div>

            {/* Location */}
            <div className="mt-6 flex items-center gap-2 text-xs font-medium text-[#A3ADB5]">
              <MapPin className="w-3.5 h-3.5 text-[#78A99B]" />
              <span>{content.location}</span>
              <span>•</span>
              <span>{lang === 'ar' ? 'خبرة في قطاعات التصنيع، الألعاب، والتجارة الإلكترونية' : 'Manufacturing, Gaming & E-Commerce Analytics'}</span>
            </div>

          </div>

          {/* Profile Image - Refined & Minimal */}
          <div className="lg:col-span-4 flex justify-center">
            <div className="relative group w-52 sm:w-60 lg:w-64">
              
              <div className="rounded-2xl bg-[#191C1F] p-2 border border-[#30363B] shadow-lg overflow-hidden">
                <img
                  src="/assets/profile.jpg"
                  alt={content.name}
                  className="w-full h-[260px] sm:h-[300px] object-cover rounded-xl transition-transform duration-500 group-hover:scale-103"
                />

                <div className="mt-2 p-2.5 rounded-lg bg-[#202428] text-center border border-[#30363B]">
                  <p className="text-[10px] text-[#78A99B] font-bold uppercase tracking-wider">
                    {lang === 'ar' ? 'التخصص الرئيسي' : 'Specialization'}
                  </p>
                  <p className="text-xs font-bold text-[#F1F3F4]">
                    {lang === 'ar' ? 'تحليل التكاليف والذكاء التجاري' : 'Cost & BI Analytics'}
                  </p>
                </div>
              </div>

            </div>
          </div>

        </div>
      </div>
    </section>
  );
}
