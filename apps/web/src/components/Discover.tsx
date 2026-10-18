import React, { useState, useEffect } from 'react';

const Discover: React.FC = () => {
  const [activities, setActivities] = useState<Array<any>>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch activities from API
    fetch('/api/v1/activities/')
      .then(response => response.json())
      .then(data => {
        setActivities(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching activities:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div className="p-6">Loading...</div>;
  }

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Discover Activities</h1>
      {activities.length === 0 ? (
        <p className="text-center py-8">No activities found.</p>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {activities.map((activity: any) => (
            <div key={activity.id} className="bg-white rounded-lg shadow p-4">
              <h3 className="font-semibold mb-2">{activity.title}</h3>
              <p className="text-gray-600">{activity.description}</p>
              {activity.is_placeholder && (
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

export default Discover;