import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();

const listProducts = [
  {itemId: 1, name: "Suitcase 250", price: 50, initialAvailableQuantity: 4},
  {itemId: 2, name: "Suitcase 450", price: 100, initialAvailbaleQuantity: 10},
  {itemId: 3, name: "Suitcsse 650", price: 350, initialAvailableQuantity: 2},
  {itemId: 4, name: "Suitcase 1050", price: 550, initialAvailableQuantity: 5}
];

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

function getItemById(id) {
  return listProducts.find(product => product.itemId === id);
}

async function reserveStockById(itemId, stock) {
  await setASync(`Item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? Number(stock) : 0;
}

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  //const itemId = parseInt(req.params.itemId, 10)
  const { itemId } = req.params;
  const item = getItemById(Number(itemId));

  if (!item) {
    return res.json({ status: 'Not Found'});
  }

  const currentReserved = await getCurrentReservedStockById(itemId);
  const availableStock = item.initialAvailableQuantity - currentReserved;

  if (availableStock <= 0) {
    return res.json({ status: 'Not Enough stock available', itemId });
  }

  await reserveStockById(itemId, currentReserved + 1);
  res.json({ status: "Reservation confirmed", itemId });

});

app.listen(1245);
