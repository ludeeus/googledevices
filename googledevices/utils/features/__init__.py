"""Init features."""
import abc


class Feature(abc.ABC):
    """Representation of a feature."""

    @abc.abstractmethod
    def has_feature(self):
        """Return if it has the feature."""
        pass
