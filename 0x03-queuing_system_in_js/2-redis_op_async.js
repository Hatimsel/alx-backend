import redis from 'redis';
import util from 'util';


const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', () => {
    console.log('Redis client not connected to the server');
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        if (err) {
            console.log(`Error setting the value for ${schoolName}`);
        } else {
            redis.print(`Reply: ${reply}`);
        }
    });
}

async function displaySchoolValue(schoolName) {
    const promisifyClient = util.promisify(client.get).bind(client);
    try {
        const data = await promisifyClient(schoolName);
        console.log(data);
    } catch(err) {
        console.error(`Error getting value for ${schoolName}: ${err}`);
    } finally {
        client.quit();
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
