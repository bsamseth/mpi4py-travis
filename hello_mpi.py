from mpi4py import MPI

comm = MPI.COMM_WORLD

print(f"Hello! I'm rank {comm.rank} out of {comm.size} processes.")

