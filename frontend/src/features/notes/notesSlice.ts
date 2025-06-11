import { createSlice, PayloadAction } from '@reduxjs/toolkit'

interface Note {
  id: string
  content: string
  createdAt: string
}

interface NotesState {
  items: Note[]
  loading: boolean
  error: string | null
}

const initialState: NotesState = {
  items: [],
  loading: false,
  error: null,
}

const notesSlice = createSlice({
  name: 'notes',
  initialState,
  reducers: {
    addNote: (state, action: PayloadAction<Note>) => {
      state.items.push(action.payload)
    },
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.loading = action.payload
    },
    setError: (state, action: PayloadAction<string | null>) => {
      state.error = action.payload
    },
  },
})

export const { addNote, setLoading, setError } = notesSlice.actions
export default notesSlice.reducer 