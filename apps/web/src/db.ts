import Dexie from 'dexie';

export interface Profile {
  id?: number;
  name: string;
  email?: string;
  role: 'student' | 'facilitator' | 'mentor' | 'admin';
  // other fields as needed
}

export interface Answer {
  id?: number;
  activityId: string;
  studentId: string;
  response: any;
  submittedAt: Date;
}

export interface CachedOpportunity {
  id?: number;
  opportunityId: string;
  data: any;
  cachedAt: Date;
}

export interface SyncQueueItem {
  id?: number;
  clientId: string; // client-generated ID
  type: string; // e.g., 'activity_response', 'opportunity_application'
  data: any;
  clientTimestamp: Date;
  serverTimestamp?: Date;
  status: 'pending' | 'synced' | 'failed';
}

export class VaultXDatabase extends Dexie {
  profile: Dexie.Table<Profile, number>;
  answers: Dexie.Table<Answer, number>;
  cachedOpportunities: Dexie.Table<CachedOpportunity, number>;
  syncQueue: Dexie.Table<SyncQueueItem, number>;

  constructor() {
    super('VaultXDatabase');
    this.version(1).stores({
      profile: '++id',
      answers: '++id, activityId, studentId',
      cachedOpportunities: '++id, opportunityId',
      syncQueue: '++id, clientId, type, status',
    });
  }
}

export const db = new VaultXDatabase();