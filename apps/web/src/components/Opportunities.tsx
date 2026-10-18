import React, { useState, useEffect } from 'react';

const Opportunities: React.FC = () => {
  const [opportunities, setOpportunities] = useState<Array<any>>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch opportunities from API
    fetch('/api/v1/opportunities/')
      .then(response => response.json())
      .then(data => {
        setOpportunities(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching opportunities:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div className="p-6">Loading...</div>;
  }

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Find Opportunities</h1>
      {opportunities.length === 0 ? (
        <p className="text-center py-8">No opportunities found.</p>
      ) : (
        <div className="space-y-4">
          {opportunities.map((opp: any) => (
            <div key={opp.id} className="bg-white rounded-lg shadow p-4">
              <h3 className="font-semibold mb-2">{opp.title}</h3>
              <p className="text-gray-600 mb-2">{opp.description}</p>
              <div className="flex flex-wrap gap-2 mb-2">
                {Object.keys(opp.eligibility_rules).map((key: string) => (
                  <span key={key} className="px-2 py-1 bg-blue-50 text-blue-800 text-xs rounded">
                    {key}: {String(opp.eligibility_rules[key as keyof typeof opp.eligibility_rules])}
                  </span>
                ))}
              </div>
              {opp.is_placeholder && (
                <span className="inline-block px-2 py-1 bg-yellow-100 text-yellow-800 text-xs rounded">
                  Placeholder
                </span>
              )}
              <span className="inline-block mt-2 px-2 py-1 bg-gray-200 text-gray-800 text-xs rounded">
                Last verified: {new Date(opp.last_verified_at).toLocaleDateString()}
              </span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Opportunities;