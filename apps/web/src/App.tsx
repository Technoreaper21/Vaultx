import React from 'react';
import { BrowserRouter as Router, Routes, Route, NavLink, useLocation } from 'react-router-dom';
import Home from './components/Home';
import Discover from './components/Discover';
import Learn from './components/Learn';
import Opportunities from './components/Opportunities';
import LanguageToggle from './components/LanguageToggle';
import './index.css';

const NavBar: React.FC = () => {
  const location = useLocation();
  return (
    <Router>
      <div className="min-h-screen flex flex-col bg-white">
        <header className="bg-blue-600 text-white p-4">
          <div className="flex justify-between items-center">
            <h1 className="text-xl font-bold">VaultX</h1>
            <LanguageToggle />
          </div>
        </header>

        <nav className="border-t border-b border-gray-200">
          <div className="flex">
            <NavLink
              to="/"
              className={`flex-1 text-center py-3 ${location.pathname === '/' ? 'text-blue-600 border-b-2 border-blue-600' : 'text-gray-600 hover:text-gray-800'}`}
            >
              Home
            </NavLink>
            <NavLink
              to="/discover"
              className={`flex-1 text-center py-3 ${location.pathname === '/discover' ? 'text-blue-600 border-b-2 border-blue-600' : 'text-gray-600 hover:text-gray-800'}`}
            >
              Discover
            </NavLink>
            <NavLink
              to="/learn"
              className={`flex-1 text-center py-3 ${location.pathname === '/learn' ? 'text-blue-600 border-b-2 border-blue-600' : 'text-gray-600 hover:text-gray-800'}`}
            >
              Learn
            </NavLink>
            <NavLink
              to="/opportunities"
              className={`flex-1 text-center py-3 ${location.pathname === '/opportunities' ? 'text-blue-600 border-b-2 border-blue-600' : 'text-gray-600 hover:text-gray-800'}`}
            >
              Opportunities
            </NavLink>
          </div>
        </nav>

        <main className="flex-1 p-4">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/discover" element={<Discover />} />
            <Route path="/learn" element={<Learn />} />
            <Route path="/opportunities" element={<Opportunities />} />
          </Routes>
        </main>

        <footer className="bg-gray-50 text-gray-600 text-sm p-4">
          VaultX © 2026 - For rural Indian students
        </footer>
      </div>
    </Router>
  );
};

export default NavBar;