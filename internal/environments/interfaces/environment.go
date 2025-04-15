package interfaces

import (
	"context"

	"environment/internal/domain/models"
)

type Environment interface {
	// Reset the environment to an initial state
	Reset(ctx context.Context) error

	// Process an Action & return the next State, Reward & done flag.
	Step(ctx context.Context, action models.Action) (models.State, float64, bool, error)

	// Get the State Space for this Environment.
	StateSpace() models.StateSpace
}
