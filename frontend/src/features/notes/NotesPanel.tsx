import { Box, Paper } from '@mui/material'
import { SearchBar } from '../search/SearchBar'
import { NotesList } from './NotesList'

export const NotesPanel = () => {
  return (
    <Paper 
      elevation={2} 
      sx={{ 
        height: '100%',
        display: 'flex',
        flexDirection: 'column',
        p: 2
      }}
    >
      <SearchBar />
      <Box sx={{ flexGrow: 1, overflow: 'auto' }}>
        <NotesList />
      </Box>
    </Paper>
  )
} 