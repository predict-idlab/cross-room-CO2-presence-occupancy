import numpy as np
from tsflex.features import FeatureCollection, FeatureDescriptor, MultipleFeatureDescriptors

def last(x):
    return x[-1]

def slope(signal):
    signal = signal[~np.isnan(signal)]
    if len(signal) < 2: return np.NaN

    # Source: https://github.com/fraunhoferportugal/tsfel/blob/master/tsfel/feature_extraction/features.py#L290C3-L290C3
    t = np.linspace(0, len(signal) - 1, len(signal))
    try:
        return np.polyfit(t, signal, 1)[0]
    except:
        raise

def extract_features(df_data, window_size='60min', shifts=None):
    # Init tsflex extraction.
    tsflex_extraction = FeatureCollection(
        [
            # Labels.
            FeatureDescriptor(
                series_name='presence',
                window='10min',
                stride='10min',
                function=last, # There will only be one sample in this window, so take it.
            ),
            # Features.
            MultipleFeatureDescriptors(
                series_names='CO2',
                windows=['10min'],
                strides=['10min'],
                functions=[last], # There will only be one sample in this window, so take it.
            ),
            MultipleFeatureDescriptors(
                series_names='CO2',
                windows=[window_size],
                strides=['10min'],
                functions=[np.mean, slope],
            )
        ]
    )

    # Extract features.
    df_features = tsflex_extraction.calculate([df_data], return_df=True, window_idx='end')

    # Temporal shift features.
    if shifts is not None:
        shift_columns = [c for c in df_features.columns if 'mean' in c or 'slope' in c]

        for shift in shifts:
            df_features = df_features.merge(df_features[shift_columns].shift(shift*-1).add_suffix(f'__t={shift}'), left_index=True, right_index=True)

    # List feature names.
    target_feature_names = ['presence__last__w=10m']
    input_feature_names = list(set(df_features.columns).difference(target_feature_names))

    return df_features, target_feature_names, input_feature_names

def sliding_window_normalization(df_data, window_size_days):
    df_mean = df_data.rolling(6*24*window_size_days).mean().bfill()
    df_std = df_data.rolling(6*24*window_size_days).std().bfill()

    return (df_data - df_mean) / df_std
