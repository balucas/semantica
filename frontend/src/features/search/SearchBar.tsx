import { useState } from 'react'
import { TextField, Box } from '@mui/material'
import { useQuery } from '@tanstack/react-query'
import { notesApi } from '@/api/notes'

export const SearchBar = () => {
  const [searchQuery, setSearchQuery] = useState('')

  const { refetch } = useQuery({
    queryKey: ['notes', searchQuery],
    queryFn: () => notesApi.searchNotes(searchQuery),
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