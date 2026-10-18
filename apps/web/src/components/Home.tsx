import React from 'react';

const Home: React.FC = () => {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Welcome to VaultX</h1>
      <p className="mb-4">
        Discover skills, plan learning, and find real opportunities.
      </p>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div className="bg-blue-50 p-4 rounded">
          <h3 className="font-semibold mb-2">Skills Discovery</h3>
          <p>Explore your interests and find what you're good at.</p>
        </div>
        <div className="bg-green-50 p-4 rounded">
          <h3 className="font-semibold mb-2">Learning Plans</h3>
          <p>Create personalized learning paths for your goals.</p>
        </div>
        <div className="bg-purple-50 p-4 rounded">
          <h3 className="font-semibold mb-2">Opportunities</h3>
          <p>Find scholarships, apprenticeships, and internships.</p>
        </div>
      </div>
    </div>
  );
};

export default Home;