import { Box, Container, Typography } from '@mui/material'
import { NotesList } from './features/notes/NotesList'
import { SearchBar } from './features/search/SearchBar'

function App() {
  return (
    <Container maxWidth="md">
      <Box sx={{ my: 4 }}>
        <Typography variant="h3" component="h1" gutterBottom>
          Semantica Notes
        </Typography>
        <SearchBar />
        <NotesList />
      </Box>
    </Container>
  )
}

export default App 