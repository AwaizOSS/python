const readLine = require("readline");
const rl = readLine.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const askQueston = (question) => {
  return new Promise((resolve) => rl.question(question, resolve));
}; // we wrapped the rl.questino in a promise as it was asynchronus in nature & based on just callback that is difficult to read & work with

const takeInput = async () => {
  let monsters = [];
  const no_of_monsters = Number(await askQueston("number of monsters: "));
  let power = Number(await askQueston("initial experience/power: "));
  for (let i = 0; i < no_of_monsters; i++) {
    let power = await askQueston(`power of monster ${i + 1}: `);
    let bonus = await askQueston(`bonus of monster ${i + 1}: `);
    monsters.push({
      power: Number(power),
      bonus: Number(bonus),
    });
  }
  rl.close();
  return { monsters, power, no_of_monsters };
};

const defeatMonsters = async () => {
  let { monsters, power, no_of_monsters } = await takeInput();
  monsters.sort((a, b) => a.power - b.power);
  console.log(monsters);
  for (let i = 0; i < no_of_monsters; i++) {
    if (power >= monsters[i].power) {
      console.log(`monster ${i + 1} defeated`);
      power += monsters[i].bonus;
      console.log("power", power);
    } else {
      console.log(`monster(s) from ${i + 1} cannot be defeated`);
      break;
    }
  }
};

defeatMonsters();
