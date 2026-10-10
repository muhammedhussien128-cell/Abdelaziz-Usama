import React from 'react';
import { BarChart3, Globe, Mail, Download, Sparkles } from 'lucide-react';

export default function Navbar({ lang, setLang, onOpenContact }) {
  return (
    <nav className="sticky top-0 z-50 bg-[#111315]/95 backdrop-blur-md border-b border-[#30363B] transition-colors duration-300">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16 sm:h-20">
          
          {/* Logo / Name */}
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-[#202428] border border-[#30363B] flex items-center justify-center">
              <BarChart3 className="w-5 h-5 text-[#78A99B]" />
            </div>
            <div>
              <span className="text-lg font-bold tracking-wide block text-[#F1F3F4]">
                {lang === 'ar' ? 'عبدالعزيز أسامة' : 'Abdelaziz Osama'}
              </span>
              <span className="text-xs text-[#78A99B] font-semibold flex items-center gap-1">
                <Sparkles className="w-3 h-3 inline" />
                {lang === 'ar' ? 'محلل بيانات & BI' : 'Data Analyst & BI'}
              </span>
            </div>
          </div>

          {/* Navigation Links */}
          <div className="hidden md:flex items-center gap-8 text-xs sm:text-sm font-medium text-[#A3ADB5]">
            <a href="#about" className="hover:text-[#78A99B] transition-colors">
              {lang === 'ar' ? 'نبذة عني' : 'About'}
            </a>
            <a href="#metrics" className="hover:text-[#78A99B] transition-colors">
              {lang === 'ar' ? 'الأرقام والإنجازات' : 'Metrics'}
            </a>
            <a href="#skills" className="hover:text-[#78A99B] transition-colors">
              {lang === 'ar' ? 'المهارات' : 'Skills'}
            </a>
            <a href="#projects" className="hover:text-[#78A99B] transition-colors">
              {lang === 'ar' ? 'المشاريع والتحليلات' : 'Case Studies'}
            </a>
          </div>

          {/* Actions: Lang switch, Download CV & Contact */}
          <div className="flex items-center gap-2 sm:gap-3">
            
            {/* Language Switch */}
            <button
              onClick={() => setLang(lang === 'ar' ? 'en' : 'ar')}
              className="flex items-center gap-1.5 px-3 py-2 rounded-xl bg-[#191C1F] hover:bg-[#252A2D] text-[#F1F3F4] border border-[#30363B] text-xs font-semibold transition-all"
            >
              <Globe className="w-3.5 h-3.5 text-[#78A99B]" />
              <span>{lang === 'ar' ? 'English' : 'العربية'}</span>
            </button>

            {/* Download CV PDF */}
            <a
              href="/assets/Abdelaziz_Resume.pdf"
              download="Abdelaziz Usama Mahmoud Abdelaziz Resume.pdf"
              target="_blank"
              rel="noopener noreferrer"
              className="hidden sm:flex items-center gap-1.5 px-3 py-2 rounded-xl bg-[#202428] hover:bg-[#252A2D] text-[#78A99B] border border-[#30363B] text-xs font-bold transition-all cursor-pointer"
            >
              <Download className="w-3.5 h-3.5" />
              <span>{lang === 'ar' ? 'تحميل الـ CV' : 'Download CV'}</span>
            </a>

            {/* Contact Button */}
            <button
              onClick={onOpenContact}
              className="flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-[#78A99B] hover:bg-[#8DBBAC] text-[#111315] text-xs font-bold shadow-sm transition-all"
            >
              <Mail className="w-3.5 h-3.5" />
              <span>{lang === 'ar' ? 'تواصل' : 'Contact'}</span>
            </button>

          </div>

        </div>
      </div>
    </nav>
  );
}
