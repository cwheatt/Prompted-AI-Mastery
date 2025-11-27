import 'dotenv/config';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const supabaseUrl = process.env.SUPABASE_URL;
const supabaseAnonKey = process.env.SUPABASE_ANON_KEY;

if (!supabaseUrl || !supabaseAnonKey) {
    console.error('❌ Missing environment variables:');
    console.error('SUPABASE_URL:', supabaseUrl ? 'present' : 'MISSING');
    console.error('SUPABASE_ANON_KEY:', supabaseAnonKey ? 'present' : 'MISSING');
    process.exit(1);
}

const authContent = `const supabaseUrl = "${supabaseUrl}";
const supabaseAnonKey = "${supabaseAnonKey}";

console.log('Supabase initialized');

export const supabase = window.supabase.createClient(supabaseUrl, supabaseAnonKey);
`;

const outputPath = path.join(__dirname, '../dist/auth.js');
fs.writeFileSync(outputPath, authContent);

console.log('✅ Generated auth.js successfully');