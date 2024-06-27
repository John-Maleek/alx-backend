import redis, { createClient } from "redis";

const createHash = (client) => {
  const dataSet = {
    Portland: "50",
    Seattle: "80",
    "New York": "20",
    Bogota: "20",
    Cali: "40",
    Paris: "2",
  };

  try {
    if (client) {
      Object.entries(dataSet).forEach(([key, value]) => {
        client.hset("HolbertonSchools", key, value);
        redis.print("Reply: 1");
      });
    }
  } catch (err) {
    console.log(err);
  }
};

const client = createClient();
client.on("error", (err) =>
  console.log("Redis client not connected to the server: ", err)
);
client.on("connect", () => {
  console.log("Redis client connected to the server");
  createHash(client);
  client.hgetall("HolbertonSchools", (error, result) => {
    !error && console.log(result);
  });
});
