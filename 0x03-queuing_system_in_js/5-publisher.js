import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});


function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message);
  }, time);
}

publishMessage("Hoberton Student #1 starts course", 100);
publishMessage("Hoberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Hoberton Student #3 starts course", 400);
