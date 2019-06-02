// Change YOUR_API_KEY_HERE to your apiKey
const url =
  "http://localhost:8080/api/v1/paths/40/suggested";

export async function getNews() {
  let result = await fetch(url).then(response => response.json());
  return result;
}
