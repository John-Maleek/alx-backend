import redis, { createClient } from "redis";
import { promisify } from "util";

const client = createClient();
client.on("error", (err) =>
  console.log("Redis client not connected to the server: ", err)
);
client.on("connect", () => console.log("Redis client connected to the server"));

const setNewSchool = (schoolName, value) => {
  if (client) {
    client.set(schoolName, value, (error) => {
      !error && redis.print("Reply: OK");
    });
  }
};

const displaySchoolValue = async (schoolName) => {
  const getClient = promisify(client.get).bind(client);
  try {
    const getValue = await getClient(schoolName);
    getValue && console.log(getValue);
  } catch (err) {
    console.log(err);
  }
};

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
