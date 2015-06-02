import FWCore.ParameterSet.Config as cms

process = cms.Process("myprocess")
process.load("CondCore.DBCommon.CondDBCommon_cfi")

#process.CondDBCommon.connect = 'sqlite_file:PhysicsPerformance.db'
process.CondDBCommon.connect = 'sqlite_file:PFCalibration.db'
#process.CondDBCommon.connect = 'sqlite_file:PFCalibration_2015_50ns_SiPionXXToYY_V1.db'


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource",
                            firstRun = cms.untracked.uint32(10)
                            )

# process.PoolDBOutputService.DBParameters.messageLevel = 3


process.mywriter = cms.EDAnalyzer(
  "ProducePFCalibrationObject",
  write = cms.untracked.bool(False),
  toWrite = cms.VPSet(
            cms.PSet(fType      = cms.untracked.string("PFfa_BARREL"), 
                     formula    = cms.untracked.string("[0] + [1]*( [2]*x+[3]/( [4]*sqrt([5]*x) ) )*exp([6]*x) + [7]*exp([8]*x*x)"),
                     limits     = cms.untracked.vdouble(1., 1000.),
                     parameters = cms.untracked.vdouble(1.288, -0.001512, -122.4, 24.41, 0.03438, 0.02702, -0.1956, 0.1905, -0.00008564, ) 
                    ),
            cms.PSet(fType      = cms.untracked.string("PFfb_BARREL"), 
                     formula    = cms.untracked.string("[0]+((([1]+([2]/sqrt(x)))*exp(-(x^[6]/[3])))-([4]*exp(-(x^[7]/[5]))))"),
                     limits     = cms.untracked.vdouble(1., 1000.),
                     parameters = cms.untracked.vdouble(-26.18, 27.46, 6.304, 2.818, 0.4685, 0.06192, -0.6173, -0.996,  ) 
                    ),
            cms.PSet(fType      = cms.untracked.string("PFfc_BARREL"), 
                     formula    = cms.untracked.string("[0]+((([1]+([2]/sqrt(x)))*exp(-(x^[6]/[3])))-([4]*exp(-(x^[7]/[5]))))"),
                     limits     = cms.untracked.vdouble(1., 1000.),
                     parameters = cms.untracked.vdouble(0.9658, 0.2194, -2.843, 9.094, 0.126, 0.06942, 1.638, -0.71133,  ) 
                    ),
            cms.PSet(fType      = cms.untracked.string("PFfaEta_BARREL"), 
                     formula    = cms.untracked.string("[0]+[1]*exp(-x/[2])"),
                     limits     = cms.untracked.vdouble(1., 1000.),
                     parameters = cms.untracked.vdouble(-0.00906884, -0.019761, 65.5951,  ) 
                    ),
            cms.PSet(fType      = cms.untracked.string("PFfbEta_BARREL"), 
                     formula    = cms.untracked.string("[0]+[1]*exp(-x/[2])"),
                     limits     = cms.untracked.vdouble(1., 1000.),
                     parameters = cms.untracked.vdouble(0.0630771, 0.0731011, 91.2553,  ) 
                    ),
            cms.PSet(fType      = cms.untracked.string("PFfa_ENDCAP"), 
                     formula    = cms.untracked.string("[0] + [1]*([2]+[3]*x^[4]/( [5]*sqrt([6]*x) ) )*exp([7]*x^[8]) + [9]*exp([10]*x^[11])"),
                     limits     = cms.untracked.vdouble(1., 1000.),
                     parameters = cms.untracked.vdouble(3.276, 0.1706, -36.43, 1.187, 0.4558, 0.1891, 0.3082, 1.469, -0.6944, 2.335, 1.227, -0.3418, ) 
                    ),
            cms.PSet(fType      = cms.untracked.string("PFfb_ENDCAP"), 
                     formula    = cms.untracked.string("[0]+((([1]+([2]/sqrt(x)))*exp(-(x^[6]/[3])))-([4]*exp(-(x^[7]/[5]))))"),
                     limits     = cms.untracked.vdouble(1., 1000.),
                     parameters = cms.untracked.vdouble(-26.02, 27.05, 13.0, 1.682, 0.3372, 0.002724, -0.6081, -1.828,  ) 
                    ),
            cms.PSet(fType      = cms.untracked.string("PFfc_ENDCAP"), 
                     formula    = cms.untracked.string("[0]+((([1]+([2]/sqrt(x)))*exp(-(x^[6]/[3])))-([4]*exp(-(x^[7]/[5]))))"),
                     limits     = cms.untracked.vdouble(1., 1000.),
                     parameters = cms.untracked.vdouble(1.315, 1.009, -3.545, 124.8, 0.4996, 0.4443, 2.076, -0.5171,  ) 
                    ),
            cms.PSet(fType      = cms.untracked.string("PFfaEta_ENDCAP"), 
                     formula    = cms.untracked.string("[0]+[1]*exp(-x/[2])"),
                    limits     = cms.untracked.vdouble(1., 1000.),
                     parameters = cms.untracked.vdouble(-0.00202111, -0.0197376, 22.4445,  ) 
                    ),
            cms.PSet(fType      = cms.untracked.string("PFfbEta_ENDCAP"), 
                     formula    = cms.untracked.string("[0]+((([1]+([2]/sqrt(x)))*exp(-(x^[6]/[3])))-([4]*exp(-(x^[7]/[5]))))"),
                     limits     = cms.untracked.vdouble(1., 1000.),
                     parameters = cms.untracked.vdouble(0.723559, -0.667024, -0.467125, 25.4637, 0.713308, 0.00859734, 0.826709, -1.35294, ) 
                    ),
            ),
  read = cms.untracked.bool(True),
  toRead = cms.untracked.vstring("PFfa_BARREL",
                                 "PFfa_ENDCAP",
                                 "PFfb_BARREL",
                                 "PFfb_ENDCAP",
                                 "PFfc_BARREL",
                                 "PFfc_ENDCAP",
                                 "PFfaEta_BARREL",
                                 "PFfaEta_ENDCAP",
                                 "PFfbEta_BARREL",
                                 "PFfbEta_ENDCAP") # same strings as fType
)


process.p = cms.Path(process.mywriter)

from CondCore.DBCommon.CondDBCommon_cfi import CondDBCommon
CondDBCommon.connect = 'sqlite_file:PFCalibration.db'
#CondDBCommon.connect = 'sqlite_file:PFCalibration_2015_50ns_SiPionXXToYY_V2.db'

process.PoolDBOutputService = cms.Service("PoolDBOutputService",
                                  CondDBCommon,
                                  toPut = cms.VPSet(cms.PSet(record = cms.string('PFCalibrationRcd'),
                                                             tag = cms.string('PFCalibration'),
                                                             timetype   = cms.untracked.string('runnumber')
                                                             )
                                                             ),
                                  loadBlobStreamer = cms.untracked.bool(False),
                                  #    timetype   = cms.untracked.string('lumiid')
                                  #    timetype   = cms.untracked.string('runnumber')
                                  )

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'MCRUN2_73_V9::All'
#process.GlobalTag.globaltag = 'START311_V1A::All'
#process.GlobalTag.connect   = 'sqlite_file:/afs/cern.ch/user/c/cerminar/public/Alca/GlobalTag/GR_R_311_V2.db'

process.GlobalTag.toGet = cms.VPSet(
  cms.PSet(record = cms.string("PFCalibrationRcd"),
           tag = cms.string("PFCalibration"),
           connect = cms.untracked.string("sqlite_file:PFCalibration.db")
           #connect = cms.untracked.string("sqlite_file:PFCalibration_2015_50ns_SiPionXXToYY_V2.db")
          )
)
