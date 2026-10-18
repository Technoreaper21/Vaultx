import React, { useState, useEffect } from 'react';

const Learn: React.FC = () => {
  const [careers, setCareers] = useState<Array<any>>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch careers from API
    fetch('/api/v1/careers/')
      .then(response => response.json())
      .then(data => {
        setCareers(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching careers:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div className="p-6">Loading...</div>;
  }

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Learn About Careers</h1>
      {careers.length === 0 ? (
        <p className="text-center py-8">No careers found.</p>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {careers.map((career: any) => (
            <div key={career.id} className="bg-white rounded-lg shadow p-4">
              <h3 className="font-semibold mb-2">{career.title}</h3>
              <p className="text-gray-600">{career.description}</p>
              {career.is_placeholder && (
                <span className="inline-block mt-2 px-2 py-1 bg-yellow-100 text-yellow-800 text-xs rounded">
                  Placeholder
                </span>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Learn;