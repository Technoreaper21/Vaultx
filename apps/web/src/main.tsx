import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';

// i18next setup
import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import enJson from './i18n/en.json';
import hiJson from './i18n/hi.json';

i18n
  .use(initReactI18next)
  .init({
    resources: {
      en: { translation: enJson },
      hi: { translation: hiJson }
    },
    lng: 'en', // default language
    fallbackLng: 'en',
    interpolation: {
      escapeValue: false // react already safes from xss
    }
  });

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);