import redis, { createClient } from "redis";

const client = createClient();
client.on("error", (err) =>
  console.log("Redis client not connected to the server: ", err)
);
client.on("connect", () => console.log("Redis client connected to the server"));

const listener = (message, channel) => {
  console.log(message);
  if (message === "KILL_SERVER") {
    client.unsubscribe();
    client.quit();
  }
};
client.subscribe("holberton school channel");
client.on("message", (channel, message) => {
  listener(message, channel);
});
