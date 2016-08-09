%  Relevant files

FactorForSofterEQS    0.0

InitCondFile      /n/home/external/schakrabarti/Minors_ICs/myvc3EQS0_1_100_Rperi1kpc.dat
OutputDir         /n/itc1/schakrabarti/Minors/myvc3EQS0_1_100_Rperi1

SnapshotFileBase  snapshot

EnergyFile        energy.txt
InfoFile          info.txt
TimingsFile       timings.txt
CpuFile           cpu.txt

RestartFile       restart

% CPU-time limit

TimeLimitCPU      3600000
ResubmitOn        0
ResubmitCommand   xxx

% Code options

ICFormat                  1
SnapFormat                1

ComovingIntegrationOn     0

NumFilesPerSnapshot       1
NumFilesWrittenInParallel 1

CoolingOn                 1
StarformationOn           1
 
%  Caracteristics of run

TimeBegin                 0.0
TimeMax                   2.0

Omega0                    0
OmegaLambda               0

OmegaBaryon               0
HubbleParam               0.7

BoxSize                   0
PeriodicBoundariesOn      0

% Output frequency

OutputListOn        0
OutputListFilename  /raid4/tcox/vc3vc3e_2/outputlist.txt

TimeBetSnapshot           0.05
TimeOfFirstSnapshot       0
 
CpuTimeBetRestartFile     1800.0

TimeBetStatistics         0.05

% Accuracy of time integration

TypeOfTimestepCriterion   0
	                    
ErrTolIntAccuracy         0.025

MaxSizeTimestep           0.005
MinSizeTimestep           1.0e-7

MaxRMSDisplacementFac     0.25

% Tree algorithm and force accuracy

ErrTolTheta               0.7

TypeOfOpeningCriterion    1
ErrTolForceAcc            0.005

TreeDomainUpdateFrequency 0.05

%  Parameters of SPH

DesNumNgb           64
MaxNumNgbDeviation  2

ArtBulkViscConst    0.75

InitGasTemp         10000.0

MinGasTemp          5.0
CourantFac          0.15

% Further code parameters

PartAllocFactor    5.0 
TreeAllocFactor     0.8

BufferSize              100

% System of units

UnitLength_in_cm         3.085678e21        ;  1.0 kpc
UnitMass_in_g            1.989e43           ;  1.0e10 solar masses
UnitVelocity_in_cm_per_s 1e5                ;  1 km/sec
GravityConstantInternal  0

% Softening lengths

MinGasHsmlFractional     0.0  % minimum gas smoothing in terms of the gravitational softening length

SofteningGas       0.1
SofteningHalo      0.2
SofteningDisk      0.1
SofteningBulge     0.1         
SofteningStars     0.1
SofteningBndry     0.16          % this will be the black hole particles

SofteningGasMaxPhys       0.025
SofteningHaloMaxPhys      0.05
SofteningDiskMaxPhys      0.025
SofteningBulgeMaxPhys     0.025
SofteningStarsMaxPhys     0.025
SofteningBndryMaxPhys     0.025

% Quantities for star formation and feedback

CritPhysDensity     0       %  critical physical density for star formation in
                            %  hydrogen number density in cm^(-3)

MaxSfrTimescale     4.5

CritOverDensity      57.7    %  overdensity threshold value
 
TempSupernova       3.0e8
 
TempClouds           1000.0   %  in Kelvin
FactorSN             0.1
FactorEVP           3000.0

WindEfficiency      0.005
WindEnergyFraction  0.0025 % 0.01  % this regulates the kinetic feedback
WindFreeTravelLength  20.0
WindFreeTravelDensFac 0.1




% Black Hole Specifics

MinFoFMassForNewSeed       5.
BlackHoleFeedbackFactor    0.05
SeedBlackHoleMass          1.0e-5
BlackHoleAccretionFactor   100.0
BlackHoleNgbFactor         1.0
BlackHoleActiveTime        1
BlackHoleEddingtonFactor   1.0
TimeBetBlackHoleSearch    1.1







