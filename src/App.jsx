import React, { useState } from 'react';
import Navbar from './components/Navbar';
import HeroSection from './components/HeroSection';
import MetricsOverview from './components/MetricsOverview';
import SkillsSection from './components/SkillsSection';
import CaseStudyCard from './components/CaseStudyCard';
import ProjectSteamModal from './components/ProjectSteamModal';
import ProjectCostModal from './components/ProjectCostModal';
import ProjectMisuoModal from './components/ProjectMisuoModal';
import ContactModal from './components/ContactModal';
import Footer from './components/Footer';
import { portfolioData } from './data/portfolio_content';
import { Sparkles } from 'lucide-react';

export default function App() {
  const [lang, setLang] = useState('en');
  const [activeModal, setActiveModal] = useState(null);
  const [filterCategory, setFilterCategory] = useState('all');

  const projects = portfolioData[lang].projects;

  const filteredProjects = projects.filter(p => {
    if (filterCategory === 'all') return true;
    if (filterCategory === 'gaming') return p.id === 'steam-analytics';
    if (filterCategory === 'cost') return p.id === 'cost-variance';
    if (filterCategory === 'ecommerce') return p.id === 'misuo-ecommerce';
    return true;
  });

  const scrollToProjects = () => {
    const elem = document.getElementById('projects');
    if (elem) elem.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <div className={`min-h-screen bg-[#111315] text-[#F1F3F4] ${lang === 'ar' ? 'font-cairo' : 'font-sans'}`} dir={lang === 'ar' ? 'rtl' : 'ltr'}>
      
      {/* Top Navbar */}
      <Navbar
        lang={lang}
        setLang={setLang}
        onOpenContact={() => setActiveModal('contact')}
      />

      {/* Main Content */}
      <main>
        
        {/* Hero Section */}
        <HeroSection
          lang={lang}
          onExploreProjects={scrollToProjects}
          onOpenContact={() => setActiveModal('contact')}
        />

        {/* Impact Numbers */}
        <MetricsOverview lang={lang} />

        {/* Skills & Tools */}
        <SkillsSection lang={lang} />

        {/* Case Studies / Projects Section */}
        <section id="projects" className="py-16 relative z-10 bg-[#111315]">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            
            {/* Header */}
            <div className="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-10">
              <div>
                <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-[#191C1F] border border-[#30363B] text-[#78A99B] text-xs font-semibold mb-2">
                  <Sparkles className="w-3.5 h-3.5" />
                  <span>{lang === 'ar' ? 'المشاريع والدراسات التحليلية' : 'Featured Case Studies'}</span>
                </div>
                <h2 className="text-2xl font-extrabold text-[#F1F3F4]">
                  {lang === 'ar' ? 'معرض لوحات القيادة والتحليلات المباشرة' : 'Interactive Dashboards Portfolio'}
                </h2>
                <p className="text-[#A3ADB5] text-xs sm:text-sm mt-1 max-w-xl">
                  {lang === 'ar'
                    ? 'اضغط على أي مشروع لاستكشاف الداشبورد التفاعلي والبيانات الحية المباشرة.'
                    : 'Click any project to explore live interactive data dashboards.'}
                </p>
              </div>

              {/* Filter Tabs */}
              <div className="flex flex-wrap gap-1.5 p-1.5 rounded-xl bg-[#191C1F] border border-[#30363B]">
                <button
                  onClick={() => setFilterCategory('all')}
                  className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
                    filterCategory === 'all'
                      ? 'bg-[#78A99B] text-[#111315] shadow-sm'
                      : 'text-[#A3ADB5] hover:text-[#F1F3F4]'
                  }`}
                >
                  {lang === 'ar' ? 'جميع المشاريع' : 'All Projects'}
                </button>
                <button
                  onClick={() => setFilterCategory('gaming')}
                  className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
                    filterCategory === 'gaming'
                      ? 'bg-[#78A99B] text-[#111315] shadow-sm'
                      : 'text-[#A3ADB5] hover:text-[#F1F3F4]'
                  }`}
                >
                  {lang === 'ar' ? 'تحليل الألعاب (Steam)' : 'Gaming Analytics'}
                </button>
                <button
                  onClick={() => setFilterCategory('cost')}
                  className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
                    filterCategory === 'cost'
                      ? 'bg-[#78A99B] text-[#111315] shadow-sm'
                      : 'text-[#A3ADB5] hover:text-[#F1F3F4]'
                  }`}
                >
                  {lang === 'ar' ? 'محاسبة التكاليف' : 'Cost Variance'}
                </button>
                <button
                  onClick={() => setFilterCategory('ecommerce')}
                  className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
                    filterCategory === 'ecommerce'
                      ? 'bg-[#78A99B] text-[#111315] shadow-sm'
                      : 'text-[#A3ADB5] hover:text-[#F1F3F4]'
                  }`}
                >
                  {lang === 'ar' ? 'التجارة الإلكترونية (MISUO)' : 'E-Commerce BI'}
                </button>
              </div>

            </div>

            {/* Projects Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {filteredProjects.map((project) => (
                <CaseStudyCard
                  key={project.id}
                  project={project}
                  lang={lang}
                  onOpenModal={(id) => setActiveModal(id)}
                />
              ))}
            </div>

          </div>
        </section>

      </main>

      {/* Footer */}
      <Footer lang={lang} />

      {/* Modals */}
      {activeModal === 'steam-analytics' && (
        <ProjectSteamModal lang={lang} onClose={() => setActiveModal(null)} />
      )}

      {activeModal === 'cost-variance' && (
        <ProjectCostModal lang={lang} onClose={() => setActiveModal(null)} />
      )}

      {activeModal === 'misuo-ecommerce' && (
        <ProjectMisuoModal lang={lang} onClose={() => setActiveModal(null)} />
      )}

      {activeModal === 'contact' && (
        <ContactModal lang={lang} onClose={() => setActiveModal(null)} />
      )}

    </div>
  );
}
