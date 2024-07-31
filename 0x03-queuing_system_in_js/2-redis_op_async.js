import {createClient } from 'redis';
import { promisify } from 'util';
//import * as redis from 'redis';

const client = createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

async function setNewSchool(schoolName, value) {
  try {
    await setAsync(schoolName, value);
    console.log(`Set ${schoolName} to ${value}`);
  } catch (err) {
    console.error(`Error setting value for ${schoolName}: ${err.message}`);
  }
}

async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
      console.log(`${schoolName}: ${reply}`);
  } catch (err) {
    console.error(`Error fetching value for ${schoolName}: ${err.message}`);
  }
}

(async () => {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');

//  client.quit();
})();
