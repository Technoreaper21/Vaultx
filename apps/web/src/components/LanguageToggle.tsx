import React from 'react';
import { useTranslation } from 'react-i18next';

const LanguageToggle: React.FC = () => {
  const { i18n } = useTranslation();
  const currentLang = i18n.language;
  const handleLanguageChange = (lng: string) => {
    i18n.changeLanguage(lng);
  };

  return (
    <div className="flex items-center space-x-2">
      <span className="text-sm">{i18n.t('language')}:</span>
      <button
        onClick={() => handleLanguageChange('en')}
        className={`px-3 py-1 rounded ${currentLang === 'en' ? 'bg-blue-600 text-white' : 'bg-gray-200 hover:bg-gray-300'}`}
      >
        {i18n.t('english')}
      </button>
      <button
        onClick={() => handleLanguageChange('hi')}
        className={`px-3 py-1 rounded ${currentLang === 'hi' ? 'bg-blue-600 text-white' : 'bg-gray-200 hover:bg-gray-300'}`}
      >
        {i18n.t('hindi')}
      </button>
    </div>
  );
};

export default LanguageToggle;