import axios from 'axios'

const API_URL = 'http://localhost:5000'

export interface Note {
  id: string
  content: string
  createdAt: string
}

export const notesApi = {
  uploadNote: async (content: string) => {
    const response = await axios.post(`${API_URL}/upload`, {
      username: 'user', // TODO: Get from auth
      actual_data: content,
    })
    return response.data
  },

  searchNotes: async (query: string) => {
    const response = await axios.get(`${API_URL}/query`, {
      params: { q: query },
    })
    return response.data
  },
} 