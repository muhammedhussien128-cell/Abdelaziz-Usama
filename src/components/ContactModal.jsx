import React, { useState } from 'react';
import { X, Mail, MapPin, Copy, Check, Send } from 'lucide-react';
import { portfolioData } from '../data/portfolio_content';

export default function ContactModal({ lang, onClose }) {
  const info = portfolioData[lang].personal;
  const [copied, setCopied] = useState(false);
  const [submitted, setSubmitted] = useState(false);

  const handleCopyEmail = () => {
    navigator.clipboard.writeText(info.email);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);
    setTimeout(() => {
      setSubmitted(false);
      onClose();
    }, 1800);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md">
      <div className="relative w-full max-w-sm bg-[#191C1F] border border-[#30363B] rounded-2xl p-5 space-y-3 shadow-2xl text-[#F1F3F4]">
        
        {/* Close button */}
        <button
          onClick={onClose}
          className="absolute top-4 left-4 w-7 h-7 rounded-lg bg-[#202428] border border-[#30363B] text-[#A3ADB5] hover:text-[#F1F3F4] flex items-center justify-center"
        >
          <X className="w-4 h-4" />
        </button>

        {/* Modal Header */}
        <div className="text-center mb-4">
          <div className="w-10 h-10 rounded-xl bg-[#202428] border border-[#30363B] mx-auto flex items-center justify-center mb-2">
            <Mail className="w-5 h-5 text-[#78A99B]" />
          </div>
          <h3 className="text-base font-bold text-[#F1F3F4]">
            {lang === 'ar' ? 'تواصل مع عبدالعزيز أسامة' : 'Contact Abdelaziz Osama'}
          </h3>
          <p className="text-xs text-[#A3ADB5] mt-1">
            {lang === 'ar' ? 'يسعدني مناقشة فرص العمل، الاستشارات، ومشاريع تحليل البيانات' : 'Open for full-time roles, BI consulting & project inquiries'}
          </p>
        </div>

        {/* Contact Info */}
        <div className="space-y-2 mb-4">
          <div className="flex items-center justify-between p-2.5 rounded-xl bg-[#202428] border border-[#30363B]">
            <div className="flex items-center gap-2">
              <Mail className="w-4 h-4 text-[#78A99B]" />
              <span className="text-xs font-semibold text-[#F1F3F4]">{info.email}</span>
            </div>
            <button
              onClick={handleCopyEmail}
              className="p-1 rounded bg-[#191C1F] text-[#A3ADB5] hover:text-[#F1F3F4] text-xs flex items-center gap-1 border border-[#30363B]"
            >
              {copied ? <Check className="w-3.5 h-3.5 text-[#81C784]" /> : <Copy className="w-3.5 h-3.5" />}
            </button>
          </div>

          <div className="flex items-center gap-2 p-2.5 rounded-xl bg-[#202428] border border-[#30363B] text-xs font-semibold text-[#F1F3F4]">
            <MapPin className="w-4 h-4 text-[#78A99B]" />
            <span>{info.location}</span>
          </div>
        </div>

        {/* Form */}
        <form onSubmit={handleSubmit} className="space-y-3">
          <div>
            <label className="block text-[11px] font-semibold text-[#A3ADB5] mb-1">
              {lang === 'ar' ? 'الاسم / الشركة' : 'Name / Company'}
            </label>
            <input
              required
              type="text"
              placeholder={lang === 'ar' ? 'مثال: أثر للاستشارات' : 'e.g. Acme Inc'}
              className="w-full px-3 py-2 rounded-lg bg-[#202428] border border-[#30363B] text-xs text-[#F1F3F4] placeholder-[#A3ADB5] focus:outline-none focus:border-[#78A99B]"
            />
          </div>

          <div>
            <label className="block text-[11px] font-semibold text-[#A3ADB5] mb-1">
              {lang === 'ar' ? 'تفاصيل الرسالة' : 'Message'}
            </label>
            <textarea
              required
              rows={3}
              placeholder={lang === 'ar' ? 'اكتب الرسالة هنا...' : 'Write message...'}
              className="w-full px-3 py-2 rounded-lg bg-[#202428] border border-[#30363B] text-xs text-[#F1F3F4] placeholder-[#A3ADB5] focus:outline-none focus:border-[#78A99B]"
            />
          </div>

          <button
            type="submit"
            className="w-full py-2.5 rounded-xl bg-[#78A99B] hover:bg-[#8DBBAC] text-[#111315] font-bold text-xs flex items-center justify-center gap-2 transition-all shadow-sm"
          >
            {submitted ? (
              <span className="text-[#111315] flex items-center gap-1.5 font-bold">
                <Check className="w-4 h-4" /> {lang === 'ar' ? 'تم الإرسال بنجاح!' : 'Sent Successfully!'}
              </span>
            ) : (
              <>
                <Send className="w-3.5 h-3.5" />
                <span>{lang === 'ar' ? 'إرسال الرسالة' : 'Send Message'}</span>
              </>
            )}
          </button>
        </form>

      </div>
    </div>
  );
}
