import { useState } from 'react'
import { TextField, Box } from '@mui/material'
import { useQuery } from '@tanstack/react-query'
import { useDispatch } from 'react-redux'
import { notesApi } from '@/api/notes'
import { setNotes, setLoading, setError } from '../notes/notesSlice'

export const SearchBar = () => {
  const [searchQuery, setSearchQuery] = useState('')
  const dispatch = useDispatch()

  const { refetch } = useQuery({
    queryKey: ['notes', searchQuery],
    queryFn: async () => {
      try {
        dispatch(setLoading(true))
        const result = await notesApi.searchNotes(searchQuery)
        // Update Redux store with search results
        dispatch(setNotes(result.db_query_results))
        return result
      } catch (error) {
        dispatch(setError(error instanceof Error ? error.message : 'An error occurred'))
        throw error
      } finally {
        dispatch(setLoading(false))
      }
    },
    enabled: false,
  })

  const handleSearch = (event: React.ChangeEvent<HTMLInputElement>) => {
    const query = event.target.value
    setSearchQuery(query)
    if (query.trim()) {
      refetch()
    }
  }

  return (
    <Box sx={{ mb: 4 }}>
      <TextField
        fullWidth
        label="Search notes"
        variant="outlined"
        value={searchQuery}
        onChange={handleSearch}
        placeholder="Type to search..."
      />
    </Box>
  )
} 