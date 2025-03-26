import axios from 'axios'

export async function checkHealth() {
  try {
    const res = await axios.get('http://localhost:8000/health')
    console.log('[health] ✅', res.data)
  } catch (error) {
    console.error('Error')
  }
}
