import { Box, Container, Grid, Paper, Typography } from '@mui/material'
import { NotesPanel } from './features/notes/NotesPanel'

function App() {
  return (
    <Container maxWidth="xl" sx={{ height: '100vh', py: 2 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        Semantica Notes
      </Typography>
      <Grid container spacing={2} sx={{ height: 'calc(100% - 60px)' }}>
        {/* Left Panel - Notes List and Search */}
        <Grid item xs={12} md={4}>
          <NotesPanel />
        </Grid>
        
        {/* Right Panel - Editor (placeholder) */}
        <Grid item xs={12} md={8}>
          <Paper 
            elevation={2} 
            sx={{ 
              height: '100%',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              p: 2
            }}
          >
            <Typography variant="h6" color="text.secondary">
              Editor Coming Soon
            </Typography>
          </Paper>
        </Grid>
      </Grid>
    </Container>
  )
}

export default App 