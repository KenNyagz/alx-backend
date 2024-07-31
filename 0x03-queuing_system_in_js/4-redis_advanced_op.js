import { createClient, print } from 'redis';


const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

function creatHash() {
  const hashKey = 'HolbertonSchools';
  const hashValues = {
    Portland: 50,
    Seattle: 80,
    NewYork: 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2
  };

  for (const [field, value] of Object.entries(hashValues)) {
    client.hset(hashKey, field, value, print);
  }
}

function displayHash() {
  client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
      console.error(`Error fetching hash: ${err.message}`);
    } else {
      console.log('Hash stored in Redis:');
      console.log(reply);
    }
  });
}

creatHash();
displayHash();

client.quit();
