import React from 'react';
import { BarChart3 } from 'lucide-react';

export default function Footer({ lang }) {
  return (
    <footer className="bg-[#111315] border-t border-[#30363B] py-6 text-center text-xs text-[#A3ADB5]">
      <div className="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-3">
        
        <div className="flex items-center gap-2">
          <BarChart3 className="w-4 h-4 text-[#78A99B]" />
          <span className="font-bold text-[#F1F3F4]">
            {lang === 'ar' ? 'عبدالعزيز أسامة محمود' : 'Abdelaziz Osama Mahmoud'}
          </span>
          <span>© {new Date().getFullYear()}</span>
        </div>

        <p className="text-[#A3ADB5]">
          {lang === 'ar' ? 'معرض أعمال تحليل البيانات ومحاسبة التكاليف' : 'Data Analytics & Cost BI Portfolio'}
        </p>

      </div>
    </footer>
  );
}
